from request_utils import create_status_message, needs_attention
from support_tools.priority import format_priority


message = create_status_message("Password reset", False)
print(message)

attention_required = needs_attention(60)
print(f"Needs attention: {attention_required}")

clean_priority = format_priority("  critical  ")
print(f"Priority: {clean_priority}")