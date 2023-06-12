#!/usr/bin/env python3

# Imports
from langchain.tools import BaseTool
from typing import Optional, Type
from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from pydantic import BaseModel, Field
from .core.loader import CodeLoader

# Define the input schema for the tool
class CodeAnalysisInput(BaseModel):
    repo_url: Optional[str] = Field(None, description="URL of the repository to analyze")
    current_directory: Optional[bool] = Field(None, description="Analyze code from the current directory")
    repo_path: Optional[str] = Field(None, description="Path to the local repository to analyze")

class CodeAnalyzerTool(BaseTool):
    name = "CodeAnalyzer"
    description = "Analyzes a code repository and provides insights"
    args_schema: Type[BaseModel] = CodeAnalysisInput

    def _run(self, repo_url: Optional[str], current_directory: Optional[bool], repo_path: Optional[str], run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        """Use CodeAnalyzerTool."""
        if repo_url:
            loader = CodeLoader(repo_url)
            code_chunks = loader.load_repository()
            return f"Analysis of repository {repo_url} completed successfully. Loaded {len(code_chunks)} code chunks."
        elif current_directory:
            loader = CodeLoader('.')
            code_chunks = loader.load_repository()
            return f"Analysis of current directory completed successfully. Loaded {len(code_chunks)} code chunks."
        elif repo_path:
            loader = CodeLoader(repo_path)
            code_chunks = loader.load_repository()
            return f"Analysis of repository at {repo_path} completed successfully. Loaded {len(code_chunks)} code chunks."
        else:
            return "No valid input provided."        

    async def _arun(self, repo_url: Optional[str], current_directory: Optional[bool], repo_path: Optional[str], run_manager: Optional[AsyncCallbackManagerForToolRun] = None) -> str:
        """Use the tool asynchronously."""
        # Here you would put the logic to analyze the repository asynchronously
        # For the sake of this example, we will just return a dummy string
        if repo_url:
            return f"Analysis of repository {repo_url} completed successfully."
        elif current_directory:
            return f"Analysis of current directory completed successfully."
        elif repo_path:
            return f"Analysis of repository at {repo_path} completed successfully."
        else:
            return "No valid input provided."
