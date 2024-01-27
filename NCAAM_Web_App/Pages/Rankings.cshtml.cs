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

        public async Task OnGetAsync(string sortOrder)
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

            switch (sortOrder)
            {
                case "srs":
                    teams = teams.OrderByDescending(s => s.SRS);
                    break;
                case "dsrs":
                    teams = teams.OrderByDescending(s => s.DSRS);
                    break;
                case "osrs":
                    teams = teams.OrderByDescending(s => s.OSRS);
                    break;
                case "ap":
                    teams = teams.Where(x=>x.APRank!=0).OrderBy(s => s.APRank);
                    break;
                case "w":
                    teams = teams.OrderByDescending(s => s.W);
                    break;
                case "l":
                    teams = teams.OrderBy(s => s.W);
                    break;
                default:
                    teams = teams.OrderBy(s => s.Ranking);
                    break;
            }

            Conferences = new SelectList(await conferenceQuery.Distinct().ToListAsync());
            Ranks = await teams.ToListAsync();
        }
    }
}