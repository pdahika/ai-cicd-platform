import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_fix(issue_payload: dict):
    """
    Generate a fix for the given issue using OpenAI API.
    
    Args:
        issue_payload: Dictionary containing issue details
        
    Returns:
        Dictionary containing the generated fix
    """
    issue_description = issue_payload.get("description", "")
    issue_context = issue_payload.get("context", "")
    
    prompt = f"""You are a code fix assistant. Analyze the following issue and provide a fix.

Issue Description:
{issue_description}

Context:
{issue_context}

Please provide a clear, concise fix with code if applicable."""
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert code fixer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    
    return {
        "status": "success",
        "fix": response.choices[0].message.content,
        "model": "gpt-4",
        "metadata": {
            "tokens_used": response.usage.total_tokens
        }
    }