# DynamicSimulation.ComputeSimulation Method

Parent Object: [DynamicSimulation](../DynamicSimulation/DynamicSimulation.md)

## Description

Computes the simulation starting at the current time step and ending at the specified time step.

## Syntax

DynamicSimulation.**ComputeSimulation**( [***EndStep***] As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EndStep | Long | Input Long that specifies the ending time step of the compute. If not specified then the last time step of the simulation is used. If a value greater than the number of time steps in the simulation is specified, an error will occur. |

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