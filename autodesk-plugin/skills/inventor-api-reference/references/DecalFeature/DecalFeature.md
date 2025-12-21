# DecalFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The DecalFeature object represents a decal feature on a part.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DecalFeature/DecalFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../DecalFeature/DecalFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../DecalFeature/DecalFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../DecalFeature/DecalFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../DecalFeature/DecalFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../DecalFeature/DecalFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../DecalFeature/DecalFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../DecalFeature/DecalFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../DecalFeature/DecalFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../DecalFeature/DecalFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../DecalFeature/DecalFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DecalFeature/DecalFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ChainFaces](../DecalFeature/DecalFeature_ChainFaces.md) | Specifies if the decal is also applied on any faces that are adjacent to the primary face. |
| [ConsumeInputs](../DecalFeature/DecalFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../DecalFeature/DecalFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Face](../DecalFeature/DecalFeature_Face.md) | Gets and sets the primary face on which the decal is applied. |
| [Faces](../DecalFeature/DecalFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../DecalFeature/DecalFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../DecalFeature/DecalFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [Image](../DecalFeature/DecalFeature_Image.md) | Gets and sets the sketch image used to apply the decal. |
| [IsOwnedByFeature](../DecalFeature/DecalFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../DecalFeature/DecalFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../DecalFeature/DecalFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../DecalFeature/DecalFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../DecalFeature/DecalFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../DecalFeature/DecalFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../DecalFeature/DecalFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../DecalFeature/DecalFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../DecalFeature/DecalFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../DecalFeature/DecalFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../DecalFeature/DecalFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WrapFace](../DecalFeature/DecalFeature_WrapFace.md) | Specifies if the decal is wrapped on the faces on which it is applied. |

## Accessed From

[DecalFeatureProxy.NativeObject](../DecalFeatureProxy/DecalFeatureProxy_NativeObject.md), [DecalFeatures.Add](../DecalFeatures/DecalFeatures_Add.md), [DecalFeatures.Item](../DecalFeatures/DecalFeatures_Item.md)

## Derived Classes

[DecalFeatureProxy](../DecalFeatureProxy/DecalFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |

## Version

Introduced in version 6
