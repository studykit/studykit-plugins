# BendPartFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The BendPartFeature object represents an existing bend part feature in an Inventor part document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BendPartFeature/BendPartFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [Edit](../BendPartFeature/BendPartFeature_Edit.md) | Method that edits the bend part feature using the new inputs. |
| [GetReferenceKey](../BendPartFeature/BendPartFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../BendPartFeature/BendPartFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../BendPartFeature/BendPartFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../BendPartFeature/BendPartFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../BendPartFeature/BendPartFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../BendPartFeature/BendPartFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../BendPartFeature/BendPartFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../BendPartFeature/BendPartFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../BendPartFeature/BendPartFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../BendPartFeature/BendPartFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BendPartFeature/BendPartFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BendInSketchNormalDirection](../BendPartFeature/BendPartFeature_BendInSketchNormalDirection.md) | Property that gets and sets the bend direction. |
| [BendLine](../BendPartFeature/BendPartFeature_BendLine.md) | Property that gets and sets the sketch line that represents the bend line. |
| [BendMinimum](../BendPartFeature/BendPartFeature_BendMinimum.md) | Property that gets and sets whether minimum bend should be applied. |
| [BendPartType](../BendPartFeature/BendPartFeature_BendPartType.md) | Property that returns the type of the bend part feature. The valid return values are kArcLengthAndAngleBendPart, kRadiusAndAngleBendPart and kRadiusAndArcLengthBendPart. |
| [BendSide](../BendPartFeature/BendPartFeature_BendSide.md) | Property that gets and sets the bend side. |
| [ConsumeInputs](../BendPartFeature/BendPartFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../BendPartFeature/BendPartFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../BendPartFeature/BendPartFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../BendPartFeature/BendPartFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../BendPartFeature/BendPartFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InputOne](../BendPartFeature/BendPartFeature_InputOne.md) | Input Variant that defines the first input for the bend arc. |
| [InputTwo](../BendPartFeature/BendPartFeature_InputTwo.md) | Input Variant that defines the second input for the bend arc. |
| [IsOwnedByFeature](../BendPartFeature/BendPartFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../BendPartFeature/BendPartFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../BendPartFeature/BendPartFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../BendPartFeature/BendPartFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../BendPartFeature/BendPartFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../BendPartFeature/BendPartFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../BendPartFeature/BendPartFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../BendPartFeature/BendPartFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../BendPartFeature/BendPartFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../BendPartFeature/BendPartFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../BendPartFeature/BendPartFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BendPartFeatureProxy.NativeObject](../BendPartFeatureProxy/BendPartFeatureProxy_NativeObject.md), [BendPartFeatures.Add](../BendPartFeatures/BendPartFeatures_Add.md), [BendPartFeatures.Item](../BendPartFeatures/BendPartFeatures_Item.md)

## Derived Classes

[BendPartFeatureProxy](../BendPartFeatureProxy/BendPartFeatureProxy.md)

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |