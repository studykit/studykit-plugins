# RectangularPatternFeatureProxy Object

Derived from: [RectangularPatternFeature](../RectangularPatternFeature/RectangularPatternFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_AddParticipant.md) | Add the specified occurrence from the list of participants for this feature. This method only applies to assembly features. |
| [Delete](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Definition.md) | Read-write property that gets and sets the RectangularPatternFeatureDefinition object associated with this feature. |
| [ExtendedName](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [PatternElements](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_PatternElements.md) | Property that returns the collection that contains the elements created by this pattern. |
| [RangeBox](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [SurfacesOpaque](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_SurfacesOpaque.md) | Gets and sets whether all the resulting surfaces are opaque or transparent. |
| [SurfacesVisible](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_SurfacesVisible.md) | Gets and sets whether all the resulting surfaces are visible or not. |
| [Type](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |