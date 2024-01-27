using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using NCAAM_Web_App.Models;

namespace NCAAM_Web_App.Pages
{
    public class OutlookModel : PageModel
    {
        private readonly NCAAM_Web_App.Data.NCAAMContext _context;

        private readonly ILogger<PrivacyModel> _logger;

        public OutlookModel(NCAAM_Web_App.Data.NCAAMContext context, ILogger<PrivacyModel> logger)
        {
            _context = context;
            _logger = logger;
        }

        public IList<Tournament> Tournaments { get; set; } = default!;

        [BindProperty(SupportsGet = true)]
        public string? SearchString { get; set; }

        public SelectList? Years { get; set; }

        [BindProperty(SupportsGet = true)]
        public string? Year { get; set; }

        public async Task OnGetAsync()
        {
            /*IQueryable<string> yearQuery = from m in _context.Year
                                            orderby m.Conference
                                            select m.Conference;

            var teams = from m in _context.Year
                         select m;
            if (!string.IsNullOrEmpty(SearchString))
            {
                teams = teams.Where(s => s.Year.Contains(SearchString));
            }
            if (!string.IsNullOrEmpty(Year))
            {
                teams = teams.Where(x => x.Year == Year);
            }

            Years = new SelectList(await yearQuery.Distinct().ToListAsync());
            Tournaments = await teams.ToListAsync();*/
        }
    }
}