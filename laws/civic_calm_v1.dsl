# Civic Calm v1 Law Pack

# Hard Constraints
BLOCK_IF contains_pii
REQUIRE postage_stamp_valid ELSE BLOCK
REQUIRE has_sources(1) ELSE LABEL "needs_sources" IF topic_is(health) OR topic_is(public_safety)
BLOCK_IF ai_media_unlabeled AND topic_is(public_safety)
BLOCK_IF contains_emergency_claim AND NOT has_sources(1)

# Ranking Rules
BOOST_IF has_attestation(city_official) weight 0.9
BOOST_IF has_attestation(utility_provider) weight 0.8
BOOST_IF has_sources(2) weight 0.4
DOWNRANK_IF rage_features_score > 0.6 weight 0.7
BOOST_IF jurisdiction_matches weight 0.6
BOOST_IF geo_within weight 0.5

# Scoring Formula
SCORE = w1*trust + w2*recency + w3*locality + w4*sources - w5*rage

# Explainability Templates
EXPLAIN "Blocked due to PII" IF contains_pii
EXPLAIN "Missing valid postage stamp" IF NOT postage_stamp_valid
EXPLAIN "Needs sources" IF has_sources(0) AND (topic_is(health) OR topic_is(public_safety))
EXPLAIN "Boosted for official attestation" IF has_attestation(city_official)
EXPLAIN "Boosted for local relevance" IF jurisdiction_matches OR geo_within