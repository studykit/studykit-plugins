# ExtrudeFeatureProxy Object

Derived from: [ExtrudeFeature](../ExtrudeFeature/ExtrudeFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_AddParticipant.md) | Method that adds the specified participant to the assembly feature. This method fails for features in a part. |
| [Delete](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Definition.md) | Read-write property that gets and sets the ExtrudeDefinition object associated with this feature. |
| [EndFaces](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_EndFaces.md) | Property that returns the set of that cap one end of the extrusion. |
| [ExtendedName](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SideFaces](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_SideFaces.md) | Property that returns a object that provides access to all of the faces created around the perimeter of the feature. |
| [StartFaces](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_StartFaces.md) | Property that returns the set of that cap one end of the extrusion and are coincident with the sketch plane. In the case of a symmetric extrusion these faces are the ones on the positive normal side of the sketch plane. In the case where there aren't any start faces this property will return Nothing. |
| [Suppressed](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ExtrudeFeatureProxy/ExtrudeFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |