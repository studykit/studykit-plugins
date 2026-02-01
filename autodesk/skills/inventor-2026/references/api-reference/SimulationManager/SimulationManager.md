# SimulationManager Object

## Description

SimulationManager Object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SimulationManager/SimulationManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DynamicSimulations](../SimulationManager/SimulationManager_DynamicSimulations.md) | Gets the DynamicSimulations object. This object provides access to the existing dynamic simulations in this document and provides the ability to create new simulations. |
| [Parent](../SimulationManager/SimulationManager_Parent.md) | Gets the parent assembly or part component definition object. |
| [Type](../SimulationManager/SimulationManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.SimulationManager](../AssemblyComponentDefinition/AssemblyComponentDefinition_SimulationManager.md), [DynamicSimulation.Parent](../DynamicSimulation/DynamicSimulation_Parent.md), [WeldmentComponentDefinition.SimulationManager](../WeldmentComponentDefinition/WeldmentComponentDefinition_SimulationManager.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Play back a simulation](../../sample-programs/DesignSimulation_PlaySimulation_Sample.md) | This sample plays back an existing dynamic simulation. |

## Version

Introduced in version 2013
