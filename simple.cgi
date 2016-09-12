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
#print header;
#print start_html("cgi");
#print "Content-type: text/html";
print "Content-type:text/html\n\n";
print "<html><head><title>Welcome</title></head>\n";
print "";
print "<body>\n";


print "";

if(length $string==0){
  foreach my $key (sort(keys(%ENV))){
    print "$key = $ENV{$key}<br>\n";
  }
}else{
    if (open(my $fh, $ENV{'QUERY_STRING'})) {
      while (my $row = <$fh>) {
        chomp $row;
        print "$row\n";
      }
      } else {
      warn "Could not open file $!";
  }
  print "<hr>";
  print "<h2>Hello $first_name $last_name Welcome to CGI PROGRAMMING.</h2>";
  print "<h3>You are $age old.</h3>";

  #if(open(DATA, "< :encoding(UTF-8)", $ENV{'QUERY_STRING'})){
  #  while(<DATA>){

    #  print "$_";
    #}
  #}else{
#    warn "Could not open file '$string' $!";
#  }
}

#print end_html;
print "</body></html>\n";
