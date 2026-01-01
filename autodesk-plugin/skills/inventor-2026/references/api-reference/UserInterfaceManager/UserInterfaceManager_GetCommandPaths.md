# UserInterfaceManager.GetCommandPaths Method

Parent Object: [UserInterfaceManager](../UserInterfaceManager/UserInterfaceManager.md)

## Description

Method that returns all the paths that the given command is found in, optionally filtered to an environment.

## Remarks

The paths begin with the display name of the environment, followed by the tab and panel names. If the command is within a split button, the display name of the split button control is also included. Finally the path contains the display name of the command. Paths are comma separated.

For example, if "PartExtrudeCmd" is provided as the internal name, the returned string is: "Part > Model > Create > Extrude, Flat Pattern > Flat Pattern > Create > Extrude, Assembly > Model > Modify Assembly > Extrude, Weldment Assembly > Weld > Preparation and Machining > Extrude"

## Syntax

UserInterfaceManager.**GetCommandPaths**( ***CommandInternalName*** As String, [***Environment***] As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CommandInternalName | String | Input String that specifies the internal name of a ControlDefinition. |
| Environment | Variant | Optional input Environment object that specifies which Environment to return the paths for. If not specified, paths from all environments are returned. |

## Version

Introduced in version 2011
