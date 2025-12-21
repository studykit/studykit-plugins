# DynamicSimulation Object

## Description

The DynamicSimulation object represents a single dynamic simulation.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ComputeSimulation](../DynamicSimulation/DynamicSimulation_ComputeSimulation.md) | Computes the simulation starting at the current time step and ending at the specified time step. |
| [PlaySimulation](../DynamicSimulation/DynamicSimulation_PlaySimulation.md) | Plays the simulation between the specified time steps. The time steps being played must have already been computed. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DynamicSimulation/DynamicSimulation_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CurrentTimeStep](../DynamicSimulation/DynamicSimulation_CurrentTimeStep.md) | Gets and sets the current time step of the animation. Valid values are 1 to the LastComputedTimeStep. |
| [DSJoints](../DynamicSimulation/DynamicSimulation_DSJoints.md) | Gets the DSJoints object which provides access to all of the joints associated with this simulation. |
| [DSLoads](../DynamicSimulation/DynamicSimulation_DSLoads.md) | Gets the DSLoads object which provides access to all of the loads associated with this simulation. |
| [DSSettings](../DynamicSimulation/DynamicSimulation_DSSettings.md) | Gets the DSSettings object which provides access to settings associated with this simulation. |
| [IsInSimulationMode](../DynamicSimulation/DynamicSimulation_IsInSimulationMode.md) | Toggles the simulation between simulation and construction modes. |
| [LastComputedTimeStep](../DynamicSimulation/DynamicSimulation_LastComputedTimeStep.md) | Gets the last computed time step of the simulation. |
| [NumberOfTimeSteps](../DynamicSimulation/DynamicSimulation_NumberOfTimeSteps.md) | Gets and sets the number of time steps for the entire simulation. |
| [Parent](../DynamicSimulation/DynamicSimulation_Parent.md) | Gets the parent SimulationManager object. |
| [PlaybackSpeed](../DynamicSimulation/DynamicSimulation_PlaybackSpeed.md) | Gets and sets the speed when playing a simulation. A value of 1 indicates that every time step should be shown, a value of 5 indicates that every fifth time step should be shown, etc. |
| [SimulationLength](../DynamicSimulation/DynamicSimulation_SimulationLength.md) | Gets and sets the simulation length of the simulation in seconds. |
| [Type](../DynamicSimulation/DynamicSimulation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DSJoint.Parent](../DSJoint/DSJoint_Parent.md), [DynamicSimulations.Item](../DynamicSimulations/DynamicSimulations_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Play back a simulation](../../sample-programs/DesignSimulation_PlaySimulation_Sample.md) | This sample plays back an existing dynamic simulation. |

## Version

Introduced in version 2013
