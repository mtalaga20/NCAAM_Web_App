using System.ComponentModel.DataAnnotations;

namespace NCAAM_Web_App.Models
{
    public class Tournament
    {
        public string Year { get; set; }

        [Key]
        public string Id { get; set; }

        public long GameNum { get; set; }

        public string? Game { get; set; }

        public string? Result { get; set; }
        
    }
}
 