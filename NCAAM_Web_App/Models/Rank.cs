using System.ComponentModel.DataAnnotations;

namespace NCAAM_Web_App.Models
{
    public class Rank
    {
        public string? TeamName { get; set; }

        [Key]
        public long Ranking { get; set; }

        public long Score { get; set; }

        public string? Conference { get; set; }
        
    }
}
