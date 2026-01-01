# DesignProjectManager.ResolveFile Method

Parent Object: [DesignProjectManager](../DesignProjectManager/DesignProjectManager.md)

## Description

Method that runs the file resolver from the source path and attempts to find the destination file name, in the active project. The full file name of the resolved file is returned. A null string is returned if no file was resolved to.

## Syntax

DesignProjectManager.**ResolveFile**( ***SourcePath*** As String, ***DestinationFileName*** As String, [***Options***] As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SourcePath | String | Input String that specifies the source path to start the file resolution from. |
| DestinationFileName | String | Input String that specifies the destination file name to resolve to. This can either be a relative file name or a full file name. |
| Options | Variant | Optional input Variant reserved for future use. Currently ignored. |

## Version

Introduced in version 2011
