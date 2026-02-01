# BoundaryFillFeature Object

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

Object that represents an existing boundary fill feature in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [applyCellChanges](BoundaryFillFeature_applyCellChanges.htm) | After making any changes to the set of selected cells you must call this method to indicate all changes have been made and to apply those changes to the feature. |
| [classType](BoundaryFillFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](BoundaryFillFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](BoundaryFillFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](BoundaryFillFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](BoundaryFillFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](BoundaryFillFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](BoundaryFillFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](BoundaryFillFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [bRepCells](BoundaryFillFeature_bRepCells.htm) | Gets the set of closed boundaries that have been calculated based on the current set of tools. To get this collection the model must be in the state it was when the feature was initially computed, which means the timeline marker must be positioned to immediately before this feature.   After changing any selected cells you must call the applyCellChanges method to update the feature with the changes. |
| [entityToken](BoundaryFillFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](BoundaryFillFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](BoundaryFillFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](BoundaryFillFeature_healthState.htm) | Returns the current health state of the feature. |
| [isParametric](BoundaryFillFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isRemoveTools](BoundaryFillFeature_isRemoveTools.htm) | Gets and sets whether any BRepBodys that were used as tools should be removed as part of the feature creation.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isSuppressed](BoundaryFillFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](BoundaryFillFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](BoundaryFillFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](BoundaryFillFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](BoundaryFillFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](BoundaryFillFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [operation](BoundaryFillFeature_operation.htm) | Gets and sets the type of operation performed by the boundary fill feature. |
| [parentComponent](BoundaryFillFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [timelineObject](BoundaryFillFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |
| [tools](BoundaryFillFeature_tools.htm) | A collection of construction planes and open or closed BRepBody objects that define the set of boundaries that have been used in the calculation of available closed boundaries. Setting this property will clear all currently selected tools.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |

## Accessed From

[BoundaryFillFeature.createForAssemblyContext](BoundaryFillFeature_createForAssemblyContext.htm), [BoundaryFillFeature.nativeObject](BoundaryFillFeature_nativeObject.htm), [BoundaryFillFeatures.add](BoundaryFillFeatures_add.htm), [BoundaryFillFeatures.item](BoundaryFillFeatures_item.htm), [BoundaryFillFeatures.itemByName](BoundaryFillFeatures_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Boundary Fill Feature API Sample](BoundaryFillFeatureSample_Sample.htm) | Demonstrates creating a new boundary fill feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |