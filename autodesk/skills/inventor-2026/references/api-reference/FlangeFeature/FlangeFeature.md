# FlangeFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The FlangeFeature object represents a sheet metal flange feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FlangeFeature/FlangeFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../FlangeFeature/FlangeFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../FlangeFeature/FlangeFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../FlangeFeature/FlangeFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../FlangeFeature/FlangeFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../FlangeFeature/FlangeFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../FlangeFeature/FlangeFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../FlangeFeature/FlangeFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../FlangeFeature/FlangeFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../FlangeFeature/FlangeFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../FlangeFeature/FlangeFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FlangeFeature/FlangeFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BendFeature](../FlangeFeature/FlangeFeature_BendFeature.md) | Property that returns the associated bend feature, if there is one. |
| [ConsumeInputs](../FlangeFeature/FlangeFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../FlangeFeature/FlangeFeature_Definition.md) | Read-only property that returns the FlangeDefinition object that provides access to all of the various settings that define this flange feature. |
| [ExtendedName](../FlangeFeature/FlangeFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../FlangeFeature/FlangeFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../FlangeFeature/FlangeFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../FlangeFeature/FlangeFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../FlangeFeature/FlangeFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../FlangeFeature/FlangeFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../FlangeFeature/FlangeFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../FlangeFeature/FlangeFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../FlangeFeature/FlangeFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../FlangeFeature/FlangeFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../FlangeFeature/FlangeFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../FlangeFeature/FlangeFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../FlangeFeature/FlangeFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../FlangeFeature/FlangeFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../FlangeFeature/FlangeFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FlangeDefinition.Parent](../FlangeDefinition/FlangeDefinition_Parent.md), [FlangeFeatures.Add](../FlangeFeatures/FlangeFeatures_Add.md), [FlangeFeatures.Item](../FlangeFeatures/FlangeFeatures_Item.md)

## Derived Classes

[FlangeFeatureProxy](../FlangeFeatureProxy/FlangeFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 5.3
