# FlangeDefinition Object

## Description

The FlangeDefinition object represents the information that defines a flange feature, not a flange feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddFlangeEdgeSet](../FlangeDefinition/FlangeDefinition_AddFlangeEdgeSet.md) | Method that adds a new flange edge set. |
| [Copy](../FlangeDefinition/FlangeDefinition_Copy.md) | Method that creates a copy of this FlangeDefinition object. The new FlangeDefinition object is independent of any feature. It can edited and used as input to edit an existing feature or to create a new flange feature. |
| [EdgeSetItem](../FlangeDefinition/FlangeDefinition_EdgeSetItem.md) | Method that returns the specified FlangeEdgeSet object from the collection. |
| [SetDistanceHeightExtent](../FlangeDefinition/FlangeDefinition_SetDistanceHeightExtent.md) | Method that changes the FlangeDefinition object to define a flange whose height is measured by a distance. |
| [SetFlangeAngleReferenceType](../FlangeDefinition/FlangeDefinition_SetFlangeAngleReferenceType.md) | Method that removes the override width extent for the specified physical flange. |
| [SetLegacyDistanceHeightExtent](../FlangeDefinition/FlangeDefinition_SetLegacyDistanceHeightExtent.md) | Method that changes the FlangeDefinition object to define a flange whose height is measured by a distance. The way the distance is computed for this type of height extent was used in earlier versions of Inventor and is supported in the current versions to support backward compatibility with older models. |
| [SetToHeightExtent](../FlangeDefinition/FlangeDefinition_SetToHeightExtent.md) | Method that changes the FlangeDefinition object to define a flange whose height is defined by extending to the specified entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FlangeDefinition/FlangeDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ApplyAutoMitering](../FlangeDefinition/FlangeDefinition_ApplyAutoMitering.md) | Defines if auto mitering should be performed. |
| [BendOptions](../FlangeDefinition/FlangeDefinition_BendOptions.md) | Gets and sets the bend options associated with this bend feature. |
| [BendRadius](../FlangeDefinition/FlangeDefinition_BendRadius.md) | Gets and sets the bend radius of a sheet metal flange feature. |
| [CornerOptions](../FlangeDefinition/FlangeDefinition_CornerOptions.md) | Gets and sets the CornerOptions object that defines how the corners of the bend are modeled. |
| [EdgeSetCount](../FlangeDefinition/FlangeDefinition_EdgeSetCount.md) | Read-only property that returns the flange edge set count currently defined in this flange definition. |
| [FlangeAngle](../FlangeDefinition/FlangeDefinition_FlangeAngle.md) | Gets and sets the bend angle of a sheet metal flange feature. |
| [FlangeAngleReferencePlane](../FlangeDefinition/FlangeDefinition_FlangeAngleReferencePlane.md) | Read-write property that gets and sets the reference plane(WorkPlane or Face) object that is used to define the flange angle. When set this property the WorkPlane or Face should be parallel to the flange edge, otherwise an error would occur. |
| [FlangeAngleReferenceType](../FlangeDefinition/FlangeDefinition_FlangeAngleReferenceType.md) | Read-write property that gets and sets the flange angle reference type. When change this from flange angle value type to reference plane type the SetFlangeAngleReferenceType should be used. |
| [FlangePlacementType](../FlangeDefinition/FlangeDefinition_FlangePlacementType.md) | Read-write property that gets and sets the flange placement type. |
| [HeightExtent](../FlangeDefinition/FlangeDefinition_HeightExtent.md) | Property that returns the PartFeatureExtent object that defines how the height extent of the flange feature is defined. |
| [HeightExtentType](../FlangeDefinition/FlangeDefinition_HeightExtentType.md) | Property that returns the method used to define the height extent. |
| [IsUnfoldMethodOverridden](../FlangeDefinition/FlangeDefinition_IsUnfoldMethodOverridden.md) | Read-write property that gets and set whether the unfold method has been overridden for this feature. Setting this property to False clears the override. Setting the property to True returns a failure. |
| [MiterGap](../FlangeDefinition/FlangeDefinition_MiterGap.md) | Gets and sets the miter gap size of the flange feature. |
| [Parent](../FlangeDefinition/FlangeDefinition_Parent.md) | Property that returns the parent FlangeFeature of this FlangeDefinition object. |
| [Type](../FlangeDefinition/FlangeDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldMethod](../FlangeDefinition/FlangeDefinition_UnfoldMethod.md) | Gets and sets the UnfoldMethod object that defines how the bends associated with this flange feature are unfolded. |

## Accessed From

[FlangeDefinition.Copy](../FlangeDefinition/FlangeDefinition_Copy.md), [FlangeFeature.Definition](../FlangeFeature/FlangeFeature_Definition.md), [FlangeFeatureProxy.Definition](../FlangeFeatureProxy/FlangeFeatureProxy_Definition.md), [FlangeFeatures.CreateDefinition](../FlangeFeatures/FlangeFeatures_CreateDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 2009
