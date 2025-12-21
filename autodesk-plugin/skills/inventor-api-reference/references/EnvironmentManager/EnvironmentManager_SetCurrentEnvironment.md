# EnvironmentManager.SetCurrentEnvironment Method

Parent Object: [EnvironmentManager](../EnvironmentManager/EnvironmentManager.md)

## Description

Method that sets the current Environment for this document. This is the environment that the document is currently displayed in. The change is not persisted with the document; i.e. the next time the document is opened, it will show up in its base environment or the override environment if specified.

## Syntax

EnvironmentManager.**SetCurrentEnvironment**( ***Environment*** As [Environment](../Environment/Environment.md), [***EditObjectId***] As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Environment | [Environment](../Environment/Environment.md) | Environment that the document should be displayed in. |
| EditObjectId | String |  |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Play back a simulation](../../sample-programs/DesignSimulation_PlaySimulation_Sample.md) | This sample plays back an existing dynamic simulation. |

## Version

Introduced in version 10
