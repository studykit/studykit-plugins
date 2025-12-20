# DynamicSimulation.PlaySimulation Method

Parent Object: [DynamicSimulation](../DynamicSimulation/DynamicSimulation.md)

## Description

Plays the simulation between the specified time steps. The time steps being played must have already been computed.

## Syntax

DynamicSimulation.**PlaySimulation**( [***StartStep***] As Long, [***EndStep***] As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartStep | Long | Input Long that specifies the starting time step of the playback. If not specified then the first time step of the simulation is used. This value must be less than the end time step or an error will occur. |
| EndStep | Long | Input Long that specifies the ending time step of the playback. If not specified then the last computed time step of the simulation is used. The last computed time step can be found using the LastComputedTimeStep property. If a value is specified that is greater than the last computed time step and error will occur.   This is an optional argument whose default value is -1. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Play back a simulation](../../sample-programs/DesignSimulation_PlaySimulation_Sample.md) | This sample plays back an existing dynamic simulation. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |