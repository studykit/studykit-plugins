# EnvironmentManager.GetCurrentEnvironment Method

Parent Object: [EnvironmentManager](../EnvironmentManager/EnvironmentManager.md)

## Description

Method that gets the current Environment for this document. This is the environment that the document is currently displayed in.

## Syntax

EnvironmentManager.**GetCurrentEnvironment**( ***Environment*** As [Environment](../Environment/Environment.md), ***EditTargetId*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Environment | [Environment](../Environment/Environment.md) | Output Environment that the document is currently displayed in. |
| EditTargetId | String | Output string (if available) that contains the edit target identifier if specified by the client. The string indicates the edit target associated with this instance of the environment. |

## Version

Introduced in version 10
