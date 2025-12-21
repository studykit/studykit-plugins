# BendPartFeatureProxy Object

Derived from: [BendPartFeature](../BendPartFeature/BendPartFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BendPartFeatureProxy/BendPartFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [Edit](../BendPartFeatureProxy/BendPartFeatureProxy_Edit.md) | Method that edits the bend part feature using the new inputs. |
| [GetReferenceKey](../BendPartFeatureProxy/BendPartFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../BendPartFeatureProxy/BendPartFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../BendPartFeatureProxy/BendPartFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../BendPartFeatureProxy/BendPartFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../BendPartFeatureProxy/BendPartFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../BendPartFeatureProxy/BendPartFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../BendPartFeatureProxy/BendPartFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../BendPartFeatureProxy/BendPartFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../BendPartFeatureProxy/BendPartFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../BendPartFeatureProxy/BendPartFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BendPartFeatureProxy/BendPartFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BendInSketchNormalDirection](../BendPartFeatureProxy/BendPartFeatureProxy_BendInSketchNormalDirection.md) | Property that gets and sets the bend direction. |
| [BendLine](../BendPartFeatureProxy/BendPartFeatureProxy_BendLine.md) | Property that gets and sets the sketch line that represents the bend line. |
| [BendMinimum](../BendPartFeatureProxy/BendPartFeatureProxy_BendMinimum.md) | Property that gets and sets whether minimum bend should be applied. |
| [BendPartType](../BendPartFeatureProxy/BendPartFeatureProxy_BendPartType.md) | Property that returns the type of the bend part feature. The valid return values are kArcLengthAndAngleBendPart, kRadiusAndAngleBendPart and kRadiusAndArcLengthBendPart. |
| [BendSide](../BendPartFeatureProxy/BendPartFeatureProxy_BendSide.md) | Property that gets and sets the bend side. |
| [ConsumeInputs](../BendPartFeatureProxy/BendPartFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../BendPartFeatureProxy/BendPartFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ExtendedName](../BendPartFeatureProxy/BendPartFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../BendPartFeatureProxy/BendPartFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../BendPartFeatureProxy/BendPartFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../BendPartFeatureProxy/BendPartFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InputOne](../BendPartFeatureProxy/BendPartFeatureProxy_InputOne.md) | Input Variant that defines the first input for the bend arc. |
| [InputTwo](../BendPartFeatureProxy/BendPartFeatureProxy_InputTwo.md) | Input Variant that defines the second input for the bend arc. |
| [IsOwnedByFeature](../BendPartFeatureProxy/BendPartFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../BendPartFeatureProxy/BendPartFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../BendPartFeatureProxy/BendPartFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../BendPartFeatureProxy/BendPartFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../BendPartFeatureProxy/BendPartFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../BendPartFeatureProxy/BendPartFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../BendPartFeatureProxy/BendPartFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../BendPartFeatureProxy/BendPartFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../BendPartFeatureProxy/BendPartFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../BendPartFeatureProxy/BendPartFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../BendPartFeatureProxy/BendPartFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../BendPartFeatureProxy/BendPartFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2008
