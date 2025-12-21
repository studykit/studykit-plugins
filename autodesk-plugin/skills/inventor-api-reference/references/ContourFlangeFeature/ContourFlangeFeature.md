# ContourFlangeFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The ContourFlangeFeature object represents a sheet metal contour flange feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ContourFlangeFeature/ContourFlangeFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ContourFlangeFeature/ContourFlangeFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ContourFlangeFeature/ContourFlangeFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ContourFlangeFeature/ContourFlangeFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ContourFlangeFeature/ContourFlangeFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ContourFlangeFeature/ContourFlangeFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ContourFlangeFeature/ContourFlangeFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ContourFlangeFeature/ContourFlangeFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ContourFlangeFeature/ContourFlangeFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ContourFlangeFeature/ContourFlangeFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ContourFlangeFeature/ContourFlangeFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ContourFlangeFeature/ContourFlangeFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BendFeature](../ContourFlangeFeature/ContourFlangeFeature_BendFeature.md) | Property that returns the associated bend feature, if there is one. |
| [ConsumeInputs](../ContourFlangeFeature/ContourFlangeFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../ContourFlangeFeature/ContourFlangeFeature_Definition.md) | Read-write property that gets and sets the ContourFlangeDefinition object associated with this contour flange feature. |
| [ExtendedName](../ContourFlangeFeature/ContourFlangeFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ContourFlangeFeature/ContourFlangeFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ContourFlangeFeature/ContourFlangeFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ContourFlangeFeature/ContourFlangeFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../ContourFlangeFeature/ContourFlangeFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ContourFlangeFeature/ContourFlangeFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../ContourFlangeFeature/ContourFlangeFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ContourFlangeFeature/ContourFlangeFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ContourFlangeFeature/ContourFlangeFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ContourFlangeFeature/ContourFlangeFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ContourFlangeFeature/ContourFlangeFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ContourFlangeFeature/ContourFlangeFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../ContourFlangeFeature/ContourFlangeFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ContourFlangeFeature/ContourFlangeFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ContourFlangeFeature/ContourFlangeFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ContourFlangeDefinition.Parent](../ContourFlangeDefinition/ContourFlangeDefinition_Parent.md), [ContourFlangeFeatures.Add](../ContourFlangeFeatures/ContourFlangeFeatures_Add.md), [ContourFlangeFeatures.Item](../ContourFlangeFeatures/ContourFlangeFeatures_Item.md)

## Derived Classes

[ContourFlangeFeatureProxy](../ContourFlangeFeatureProxy/ContourFlangeFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |