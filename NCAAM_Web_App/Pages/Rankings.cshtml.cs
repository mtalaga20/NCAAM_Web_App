using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using NCAAM_Web_App.Models;

namespace NCAAM_Web_App.Pages
{
    public class RankingsModel : PageModel
    {
        private readonly NCAAM_Web_App.Data.NCAAMContext _context;

        private readonly ILogger<PrivacyModel> _logger;

        public RankingsModel(NCAAM_Web_App.Data.NCAAMContext context, ILogger<PrivacyModel> logger)
        {
            _context = context;
            _logger = logger;
        }

        public IList<Rank> Ranks { get; set; } = default!;

        [BindProperty(SupportsGet = true)]
        public string? SearchString { get; set; }

        public SelectList? Conferences { get; set; }

        [BindProperty(SupportsGet = true)]
        public string? Conference { get; set; }

        public async Task OnGetAsync()
        {
            IQueryable<string> conferenceQuery = from m in _context.Rank
                                            orderby m.Conference
                                            select m.Conference;

            var teams = from m in _context.Rank
                         select m;
            if (!string.IsNullOrEmpty(SearchString))
            {
                teams = teams.Where(s => s.TeamName.Contains(SearchString));
            }
            if (!string.IsNullOrEmpty(Conference))
            {
                teams = teams.Where(x => x.Conference == Conference);
            }

            Conferences = new SelectList(await conferenceQuery.Distinct().ToListAsync());
            Ranks = await teams.ToListAsync();
        }
    }
}