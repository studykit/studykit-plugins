# ChamferDefinition Object

## Description

The ChamferDefinition object is the base class that defines the variables for chamfer features

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreatePartialChamferEdges](../ChamferDefinition/ChamferDefinition_CreatePartialChamferEdges.md) | Create a new transient PartialChamferEdges collection object which can be used to define the partially chamfered edges info. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Angle](../ChamferDefinition/ChamferDefinition_Angle.md) | Returns the parameter that controls the angle used for the chamfer feature. This is applicable when the DefinitionType is kDistanceAndAngle. |
| [Application](../ChamferDefinition/ChamferDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AutomaticEdgeChain](../ChamferDefinition/ChamferDefinition_AutomaticEdgeChain.md) | Gets whether or not to use all tangentially connected edges. |
| [ChamferedEdges](../ChamferDefinition/ChamferDefinition_ChamferedEdges.md) | Gets the collection of edges that are chamfered by this feature. |
| [CornerSetback](../ChamferDefinition/ChamferDefinition_CornerSetback.md) | Gets and sets whether a setback is to be applied to the chamfer feature. |
| [DefinitionType](../ChamferDefinition/ChamferDefinition_DefinitionType.md) | Gets the type of the definition object used to hold data for chamfer feature. |
| [Distance](../ChamferDefinition/ChamferDefinition_Distance.md) | Returns the parameter that controls the distance used for the chamfer feature. This is applicable when the DefinitionType is kDistance. |
| [DistanceOne](../ChamferDefinition/ChamferDefinition_DistanceOne.md) | Returns the parameter that controls the first distance used for the chamfer feature. This is applicable when the DefinitionType is kTwoDistances. |
| [DistanceTwo](../ChamferDefinition/ChamferDefinition_DistanceTwo.md) | Returns the parameter that controls the second distance used for the chamfer feature. This is applicable when the DefinitionType is kTwoDistances. |
| [Face](../ChamferDefinition/ChamferDefinition_Face.md) | Returns the face used to define the chamfer feature created using a distance and an angle or two distances. |
| [Parent](../ChamferDefinition/ChamferDefinition_Parent.md) | Property that returns the parent ChamferFeature of the definition. |
| [PartialChamferEdges](../ChamferDefinition/ChamferDefinition_PartialChamferEdges.md) | Gets and sets the PartialChamferEdges collection object which defines the partially chamfered edges info. |
| [PreserveAllFeatures](../ChamferDefinition/ChamferDefinition_PreserveAllFeatures.md) | Gets whether or not to preserve all features. |
| [Type](../ChamferDefinition/ChamferDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ChamferFeature.Definition](../ChamferFeature/ChamferFeature_Definition.md), [ChamferFeatureProxy.Definition](../ChamferFeatureProxy/ChamferFeatureProxy_Definition.md), [CornerChamferDefinition.ChamferDefinition](../CornerChamferDefinition/CornerChamferDefinition_ChamferDefinition.md), [PartialChamferEdge.Parent](../PartialChamferEdge/PartialChamferEdge_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Partial Chamfer Sample](../../sample-programs/PartialChamferSample_Sample.md) | This sample demonstrates how to edit a chamfer feature to set the partial chamfer on a chamfered edge. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |