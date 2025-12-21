# LoftFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The LoftFeature object represents an existing loft in an Autodesk Inventor part document. The LoftFeature is derived from the PartFeature object and inherits all of its methods and properties.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../LoftFeature/LoftFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../LoftFeature/LoftFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../LoftFeature/LoftFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../LoftFeature/LoftFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../LoftFeature/LoftFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../LoftFeature/LoftFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../LoftFeature/LoftFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../LoftFeature/LoftFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../LoftFeature/LoftFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../LoftFeature/LoftFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../LoftFeature/LoftFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../LoftFeature/LoftFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../LoftFeature/LoftFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../LoftFeature/LoftFeature_Definition.md) | Gets and sets the definition for the loft feature. |
| [EndFace](../LoftFeature/LoftFeature_EndFace.md) | Property that returns the that acts as the cap of the last section of the loft. This property will return nothing in the cases where the loft does not have a ending face. These cases are when the loft sections are not closed or when the loft operation does not result in a solid. |
| [ExtendedName](../LoftFeature/LoftFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../LoftFeature/LoftFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../LoftFeature/LoftFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../LoftFeature/LoftFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../LoftFeature/LoftFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../LoftFeature/LoftFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../LoftFeature/LoftFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../LoftFeature/LoftFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../LoftFeature/LoftFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../LoftFeature/LoftFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../LoftFeature/LoftFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../LoftFeature/LoftFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SideFaces](../LoftFeature/LoftFeature_SideFaces.md) | Property that returns a object that provides access to all of the faces created around the perimeter of the feature. |
| [StartFace](../LoftFeature/LoftFeature_StartFace.md) | Property that returns the that acts as the cap of the first section of the loft. This property will return nothing in the cases where the loft does not have a starting face. These cases are when the loft sections are not closed or when the loft operation does not result in a solid. |
| [Suppressed](../LoftFeature/LoftFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../LoftFeature/LoftFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../LoftFeature/LoftFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[LoftFeatureProxy.NativeObject](../LoftFeatureProxy/LoftFeatureProxy_NativeObject.md), [LoftFeatures.Add](../LoftFeatures/LoftFeatures_Add.md), [LoftFeatures.Item](../LoftFeatures/LoftFeatures_Item.md)

## Derived Classes

[LoftFeatureProxy](../LoftFeatureProxy/LoftFeatureProxy.md)

## Version

Introduced in version 5
