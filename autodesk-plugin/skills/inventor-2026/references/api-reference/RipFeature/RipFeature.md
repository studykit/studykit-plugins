# RipFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The RepFeature object represents a rip sheet metal feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RipFeature/RipFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../RipFeature/RipFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../RipFeature/RipFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../RipFeature/RipFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../RipFeature/RipFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../RipFeature/RipFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../RipFeature/RipFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../RipFeature/RipFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../RipFeature/RipFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../RipFeature/RipFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../RipFeature/RipFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RipFeature/RipFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../RipFeature/RipFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../RipFeature/RipFeature_Definition.md) | Gets and sets the RipDefinition object associated with this rip feature. Modifying the RipDefinition object will edit the associated RipFeature. |
| [ExtendedName](../RipFeature/RipFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../RipFeature/RipFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../RipFeature/RipFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../RipFeature/RipFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../RipFeature/RipFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../RipFeature/RipFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../RipFeature/RipFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../RipFeature/RipFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../RipFeature/RipFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../RipFeature/RipFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../RipFeature/RipFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../RipFeature/RipFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../RipFeature/RipFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../RipFeature/RipFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../RipFeature/RipFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[RipDefinition.Parent](../RipDefinition/RipDefinition_Parent.md), [RipFeatures.Add](../RipFeatures/RipFeatures_Add.md), [RipFeatures.Item](../RipFeatures/RipFeatures_Item.md)

## Derived Classes

[RipFeatureProxy](../RipFeatureProxy/RipFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 2010
