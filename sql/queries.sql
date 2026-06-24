-- top 5 funds by AUM
select f.scheme_name , f.fund_house, p.aum_core
from dim_fund f 
join fact_performance p 
on dim_fund.amfi_code = fact_performance.amfi_code
ORDER by amfi_code DESC
limit 5
