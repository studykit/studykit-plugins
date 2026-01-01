# HemFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The HemFeature object represents a sheet metal hem feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../HemFeature/HemFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../HemFeature/HemFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../HemFeature/HemFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../HemFeature/HemFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../HemFeature/HemFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../HemFeature/HemFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../HemFeature/HemFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../HemFeature/HemFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../HemFeature/HemFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../HemFeature/HemFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../HemFeature/HemFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../HemFeature/HemFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../HemFeature/HemFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../HemFeature/HemFeature_Definition.md) | Property that gets the HemDefinition object associated with this fold feature. |
| [ExtendedName](../HemFeature/HemFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../HemFeature/HemFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../HemFeature/HemFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../HemFeature/HemFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../HemFeature/HemFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../HemFeature/HemFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../HemFeature/HemFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../HemFeature/HemFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../HemFeature/HemFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../HemFeature/HemFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../HemFeature/HemFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../HemFeature/HemFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../HemFeature/HemFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../HemFeature/HemFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../HemFeature/HemFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[HemDefinition.Parent](../HemDefinition/HemDefinition_Parent.md), [HemFeatures.Add](../HemFeatures/HemFeatures_Add.md), [HemFeatures.Item](../HemFeatures/HemFeatures_Item.md)

## Derived Classes

[HemFeatureProxy](../HemFeatureProxy/HemFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |

## Version

Introduced in version 5.3
