using System.ComponentModel.DataAnnotations;

namespace NCAAM_Web_App.Models
{
    public class Tournament
    {
        public int Year { get; set; }

        [Key]
        public string Id { get; set; }

        public int GameNum { get; set; }

        public string? Game { get; set; }

        public string? Result { get; set; }
        
    }
}
 