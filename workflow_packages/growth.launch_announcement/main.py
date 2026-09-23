SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "email_subject": {"type": "string"},
        "email_body": {"type": "string"},
        "linkedin_post": {"type": "string"},
        "twitter_thread": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["email_subject", "email_body", "linkedin_post", "twitter_thread"]
}

async def run(ctx, inputs):
    data = {
        "release_notes": inputs["release_notes"],
        "target_audience": inputs.get("target_audience", "Existing customers and industry professionals")
    }
    
    result = await ctx.models.generate(
        route="draft_campaign",
        step="draft_announcements",
        instructions=(
            "You are an expert product marketer. Turn the provided release notes into a "
            "multi-channel launch campaign. \n"
            "1. An engaging email blast (subject and body).\n"
            "2. A professional LinkedIn post focusing on the value proposition.\n"
            "3. A concise, engaging Twitter thread (array of tweets).\n"
            "Tailor the tone to the target audience. Focus on benefits, not just features."
        ),
        data=data,
        output_schema=SCHEMA,
    )
    
    parsed = result["parsed"]
    twitter_text = "\n\n".join([f"{i+1}/ {tweet}" for i, tweet in enumerate(parsed["twitter_thread"])])
    
    content = f"""# Launch Campaign Drafts

## Email Blast
**Subject:** {parsed["email_subject"]}

{parsed["email_body"]}

---

## LinkedIn Post
{parsed["linkedin_post"]}

---

## Twitter Thread
{twitter_text}
"""
    return {
        "path": "reports/LAUNCH_ANNOUNCEMENT.md",
        "content": content
    }

