import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    # These can be overridden with environment variables
    # TRADINGAGENTS_LLM_PROVIDER, TRADINGAGENTS_BACKEND_URL,
    # TRADINGAGENTS_DEEP_THINK_LLM, and TRADINGAGENTS_QUICK_THINK_LLM
    "llm_provider": os.getenv("TRADINGAGENTS_LLM_PROVIDER", "openrouter"),
    "deep_think_llm": os.getenv(
        "TRADINGAGENTS_DEEP_THINK_LLM", "mistralai/mixtral-8x7b-instruct"
    ),
    "quick_think_llm": os.getenv(
        "TRADINGAGENTS_QUICK_THINK_LLM", "mistralai/mistral-7b-instruct"
    ),
    "backend_url": os.getenv("TRADINGAGENTS_BACKEND_URL", "https://openrouter.ai/api/v1"),
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
}
