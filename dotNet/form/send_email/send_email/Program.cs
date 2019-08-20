using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace send_email
{
    class Program
    {
        static void Main(string[] args)
        {
            string mailTopic = "";
            string mailContent = "";
            List<string> targets = new List<string>();
            targets.Add("example@email.com");

            MailService mailService = MailService.getInstance();
            mailService.sendNoticeMail(mailTopic, targets.ToArray(), null, mailContent);
        }

    }
}
