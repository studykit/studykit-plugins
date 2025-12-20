# CutFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The CutFeature object represents a sheet metal cut feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CutFeature/CutFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../CutFeature/CutFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../CutFeature/CutFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../CutFeature/CutFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../CutFeature/CutFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../CutFeature/CutFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../CutFeature/CutFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../CutFeature/CutFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../CutFeature/CutFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../CutFeature/CutFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../CutFeature/CutFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CutFeature/CutFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../CutFeature/CutFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../CutFeature/CutFeature_Definition.md) | Property that gets/sets the CutDefinition object associated with this cut feature. |
| [ExtendedName](../CutFeature/CutFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../CutFeature/CutFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../CutFeature/CutFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../CutFeature/CutFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../CutFeature/CutFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../CutFeature/CutFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../CutFeature/CutFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../CutFeature/CutFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../CutFeature/CutFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../CutFeature/CutFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../CutFeature/CutFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../CutFeature/CutFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../CutFeature/CutFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../CutFeature/CutFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../CutFeature/CutFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CutDefinition.Parent](../CutDefinition/CutDefinition_Parent.md), [CutFeatures.Add](../CutFeatures/CutFeatures_Add.md), [CutFeatures.Item](../CutFeatures/CutFeatures_Item.md)

## Derived Classes

[CutFeatureProxy](../CutFeatureProxy/CutFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |