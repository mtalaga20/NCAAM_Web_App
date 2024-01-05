using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using NCAAM_Web_App.Models;

namespace NCAAM_Web_App.Data
{
    public class NCAAMContext : DbContext
    {
        public NCAAMContext(DbContextOptions<NCAAMContext> options)
            : base(options)
        {
        }

        public DbSet<NCAAM_Web_App.Models.Rank> Rank { get; set; } = default!;
    }
}