using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using NCAAM_Web_App.Models;

namespace NCAAM_Web_App.Pages
{
    public class TournamentModel : PageModel
    {
        private readonly NCAAM_Web_App.Data.NCAAMContext _context;

        private readonly ILogger<PrivacyModel> _logger;

        public TournamentModel(NCAAM_Web_App.Data.NCAAMContext context, ILogger<PrivacyModel> logger)
        {
            _context = context;
            _logger = logger;
        }

        public IList<Tournament> Tournaments { get; set; } = default!;

        //[BindProperty(SupportsGet = true)]
        //public string? SearchString { get; set; }

        public SelectList? Years { get; set; }

        [BindProperty(SupportsGet = true)]
        public int? Year { get; set; }

        public async Task OnGetAsync()
        {
            IQueryable<int> yearQuery = from m in _context.Tournament
                                            orderby m.Year
                                            select m.Year;

            var games = from m in _context.Tournament
                        select m;
            if (!(Year == null))
            {
                games = games.Where(x => x.Year == Year);
            }

            Years = new SelectList(await yearQuery.Distinct().ToListAsync());
            Tournaments = await games.ToListAsync();
        }
    }
}