SELECT signups.user_id, COALESCE(ROUND(AVG(action='confirmed'),2),0) as confirmation_rate
FROM signups LEFT JOIN confirmations ON signups.user_id = confirmations.user_id
GROUP BY signups.user_id