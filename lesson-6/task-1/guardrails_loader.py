from nemoguardrails import LLMRails, RailsConfig

config = RailsConfig.from_path("./guardrails")

rails = LLMRails(config)