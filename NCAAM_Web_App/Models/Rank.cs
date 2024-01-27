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

        public long? APRank { get; set; }

        public long? W { get; set; }

        public long? L { get; set; }

        public double? SRS { get; set; }

        public double? OSRS { get; set; }

        public double? DSRS { get; set; }
        
    }
}
