using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using NCAAM_Web_App.Models;

namespace NCAAM_Web_App.Pages
{
    public class VersusModel : PageModel
    {
        private readonly NCAAM_Web_App.Data.NCAAMContext _context;

        private readonly ILogger<PrivacyModel> _logger;

        public VersusModel(NCAAM_Web_App.Data.NCAAMContext context, ILogger<PrivacyModel> logger)
        {
            _context = context;
            _logger = logger;
        }

        [BindProperty(SupportsGet = true)]
        public string? TeamOne { get; set; } 

        [BindProperty(SupportsGet = true)]
        public string? TeamTwo { get; set; }

        public string? Score { get; set; } = null;

        public SelectList? Teams { get; set; }

        public async Task OnGetAsync()
        {
            IQueryable<string> teamQuery = from m in _context.Rank
                                           orderby m.TeamName
                                           select m.TeamName;
            if (!string.IsNullOrEmpty(TeamOne) && !string.IsNullOrEmpty(TeamTwo))
            {
                Process process = new Process();
                process.StartInfo.FileName = "C:\\Program Files\\Python311\\python.exe";
                process.StartInfo.Arguments = $"C:\\Users\\mktal\\repos\\College_Basketball_Game_Prediction\\modeling\\team_versus.py \"{TeamOne}\" \"{TeamTwo}\""; // Note the /c command (*)
                process.StartInfo.UseShellExecute = false;
                process.StartInfo.RedirectStandardOutput = true;
                process.StartInfo.RedirectStandardError = true;
                process.Start();
                //* Read the output (or the error)
                string output = process.StandardOutput.ReadToEnd();
                Console.WriteLine(output);
                string err = process.StandardError.ReadToEnd();
                Console.WriteLine(err);
                process.WaitForExit();
                Score = output;
            }

            Teams = new SelectList(await teamQuery.Distinct().ToListAsync());
        }
    }
}