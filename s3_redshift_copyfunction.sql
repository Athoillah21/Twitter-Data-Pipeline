-- Define Table
CREATE TABLE "public"."data"(num            integer encode az64,
                             user           character varying(256) encode lzo,
                             favorite_count integer encode az64,
                             retweet_count  integer encode az64,
                             created_at     date encode az64,
                             cleaned_tweet  character varying(256) encode lzo,
                             polarity       numeric(18,0) encode az64,
                             subjectivity   numeric(18,0) encode az64);

-- Copy Function s3 to Redshift
copy public.data
from '*****'
iam_role '*****'
delimiter ','
IGNOREHEADER as 1
csv;
