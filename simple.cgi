#!/usr/bin/perl -wT

use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

my $cgi = new CGI;

my $first_name = $cgi->param('firstname');
my $last_name = $cgi->param('lastname');
my $age = $cgi->param('age');
my $string = $ENV{'QUERY_STRING'};

print "Content-type:text/html\n\n";
print "<html><head>";
print "<title>Welcome</title>";
print "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css' integrity='sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u' crossorigin='anonymous'>";
print " <link rel='stylesheet' href='../style.css' media='screen' title='no title'>";
print "</head>\n";
print "";
print "<body>\n";
print "<nav class='navbar navbar-default'>";
print "<div class='container-fluid'>";
print "<div class='navbar-header'>";
print "<h1>SimpleApp</h1>";
print "</div>";
print "</div>";
print "</nav>";

  print "<h2>Hello $first_name $last_name Welcome to CGI PROGRAMMING.</h2>";
  print "<h3>You are $age years old.</h3>";
  print "<hr>";
if(length $string==0){
  print "<h2>List of environment variables</h2>";
  foreach my $key (sort(keys(%ENV))){
    print "<pre>$key = $ENV{$key}</pre><br>\n";
  }
}else{
    if (open(my $fh, $ENV{'QUERY_STRING'})) {
     
      print "<xmp>";
      while (my $row = <$fh>) {
        chomp $row;
        print "$row\n";
      }
      
     
      } else {
      warn "Could not open file $!";
    }

}
print "</body></html>\n";
print "</xmp>";