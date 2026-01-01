# BendDefinition Object

## Description

The BendDefinition object represents all of the information that defines a bend.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../BendDefinition/BendDefinition_Copy.md) | Method that creates a copy of this BendDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BendDefinition/BendDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BendOptions](../BendDefinition/BendDefinition_BendOptions.md) | Gets and sets the BendOptions object that defines the options for a bend. |
| [BendRadius](../BendDefinition/BendDefinition_BendRadius.md) | Gets and sets the bend radius. |
| [DoubleBendType](../BendDefinition/BendDefinition_DoubleBendType.md) | Specifies if the bend is a double bend or not. |
| [Edges](../BendDefinition/BendDefinition_Edges.md) | Gets and sets the set of edges that define the location of the bend. |
| [ExtendFaces](../BendDefinition/BendDefinition_ExtendFaces.md) | Specifies if the existing faces will be extended to the bend or if a perpendicular section should be created to connect to the bend. |
| [IsDoubleBendFirstEdgeFixed](../BendDefinition/BendDefinition_IsDoubleBendFirstEdgeFixed.md) | Specify which face remains fixed and which one is extended or trimmed in the case of double bends. |
| [IsUnfoldMethodOverridden](../BendDefinition/BendDefinition_IsUnfoldMethodOverridden.md) | Read-write property that gets and set whether the unfold method has been overridden for this feature. Setting this property to False clears the override. Setting the property to True returns a failure. |
| [Parent](../BendDefinition/BendDefinition_Parent.md) | Property that returns the parent feature of this BendDefinition object. |
| [Type](../BendDefinition/BendDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldMethod](../BendDefinition/BendDefinition_UnfoldMethod.md) | Gets and sets the UnfoldMethod object that defines how this bend is unfolded. |

## Accessed From

[BendDefinition.Copy](../BendDefinition/BendDefinition_Copy.md), [BendFeature.Definition](../BendFeature/BendFeature_Definition.md), [BendFeatureProxy.Definition](../BendFeatureProxy/BendFeatureProxy_Definition.md), [BendFeatures.CreateBendDefinition](../BendFeatures/BendFeatures_CreateBendDefinition.md), [FaceFeatureDefinition.BendDefinition](../FaceFeatureDefinition/FaceFeatureDefinition_BendDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 2009
