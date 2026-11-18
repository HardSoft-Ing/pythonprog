# Lambda function examples

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

style="BlaStyle"

# Note: Multi-line expressions in "[],{}, ()" can have random indentation.
# Only the opening bracket must correctly be aligned.

def fake_get_unvalidated_arg(name, default=None):
    values = {
	"PREFIX": "ip_",
	"LAYVER_PREFIX_STYLE": style,
	"KEEP_TMP_PREFIXING_FILES": "",
    }
    return values.get(name, default)
    

lmbfunc= lambda name, default=None: {
    "PREFIX": "ip_",
    "LAYVER_PREFIX_STYLE": style,
    "KEEP_TMP_PREFIXING_FILES": "",
}.get(name, default)

print(f"function: {fake_get_unvalidated_arg('LAYVER_PREFIX_STYLE')}")
print(f"lmbfunc: {lmbfunc('LAYVER_PREFIX_STYLE')}")