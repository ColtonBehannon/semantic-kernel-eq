import asyncio
import sys

# Add the path to your local semantic-kernel directory at the start of sys.path
sys.path.insert(0, "/home/cbeh/Projects/semantic-kernel/python")

# Now, when you import semantic_kernel, it should come from your local directory
import semantic_kernel as sk
from semantic_kernel.connectors.openapi import register_openapi_plugin

# from semantic_kernel.functions.function_result import FunctionResult  # Corrected import
# import semantic_kernel as sk
# from semantic_kernel.connectors.openapi import register_openapi_plugin

if __name__ == "__main__":
    """Client"""
    kernel = sk.Kernel()

    openapi_plugin = register_openapi_plugin(kernel, "openApiPlugin", "natgas-equity.yaml")
    # variables = {
    #     "query_params": '{"limit": "5", "text": "Equinor"}',
    #     "headers": '{"Cache-Control": "no-cache", "Gen-Api-Key": "beac8ea8436b4db785af539108dfff9e"}',
    # }

    context_variables = sk.KernelArguments(
        query_params={"limit": "5", "text": "Equinor", "format": "json"},
        headers={"Cache-Control": "no-cache", "Gen-Api-Key": "beac8ea8436b4db785af539108dfff9e"},
    )

    print(openapi_plugin["GetEarningsCallNotes"])

    result = asyncio.run(
        # Call the function defined in openapi.yaml
        openapi_plugin["GetEarningsCallNotes"].invoke(kernel, arguments=context_variables)
    )

    print("Result:")
    print(result)  # This will print the result as is
