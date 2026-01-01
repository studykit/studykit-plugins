# SweepFeature Object

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeature.h>

## Description

Object that represents an existing sweep feature in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SweepFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](SweepFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](SweepFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](SweepFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](SweepFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SweepFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](SweepFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](SweepFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [distanceOne](SweepFeature_distanceOne.htm) | Gets the distance for the first side. This property returns nothing in the case where the feature is non-parametric. |
| [distanceTwo](SweepFeature_distanceTwo.htm) | Gets the distance for the second side. Returns nothing if the path is only on one side of the profile or if the sweep definition includes a guide rail or surface. It's always the distance against the normal of the profile if available. This property returns nothing in the case where the feature is non-parametric. |
| [endFaces](SweepFeature_endFaces.htm) | Property that returns the set of that cap one end of the sweep that are coincident with the sketch plane. The end faces are those not coincident to the sketch plane of the feature's profile. In the case of a symmetric revolution these faces are the ones on the negative normal side of the sketch plane. In the cases where there aren't any end faces this property will return Nothing. |
| [entityToken](SweepFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](SweepFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [extent](SweepFeature_extent.htm) | Gets and sets the sweep extent type. It defaults to PerpendicularToPathExtentType. When sweeping a solid setting the twist angle requires the solid twist axis to be set. This property is ignored when a guide rail has not been specified. |
| [faces](SweepFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [guideRail](SweepFeature_guideRail.htm) | Gets and sets the guide rail to create the sweep. This can be set to null to have a path only sweep.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [guideSurfaces](SweepFeature_guideSurfaces.htm) | Gets and sets the guide surfaces to create the sweep. This can be set to an empty array to remove the guide surfaces and have a single path sweep feature. The isChainSelection property controls whether tangentially connected faces to the guide surfaces are also made guide surfaces.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [healthState](SweepFeature_healthState.htm) | Returns the current health state of the feature. |
| [isChainSelection](SweepFeature_isChainSelection.htm) | Get and sets whether faces that are tangentially connected to the guide surfaces are also made guide surfaces. |
| [isDirectionFlipped](SweepFeature_isDirectionFlipped.htm) | Gets and sets if the direction of the sweep is flipped. This property only applies to sweep features that include a guide rail and whose path runs on both sides of the profile.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isParametric](SweepFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSolid](SweepFeature_isSolid.htm) | Indicates if this feature was initially created as a solid or a surface. |
| [isSuppressed](SweepFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](SweepFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](SweepFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](SweepFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](SweepFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](SweepFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [operation](SweepFeature_operation.htm) | Gets and sets the type of operation performed by the sweep. |
| [orientation](SweepFeature_orientation.htm) | Gets and sets the sweep orientation. It defaults to PerpendicularOrientationType. This property is ignored if sweeping a solid or a guide rail or surface has been specified.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [parentComponent](SweepFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [participantBodies](SweepFeature_participantBodies.htm) | Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [path](SweepFeature_path.htm) | Gets and sets the path to create the sweep. This property returns nothing in the case where the feature is non-parametric.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [profile](SweepFeature_profile.htm) | Gets and sets the profiles or planar faces used to define the shape of the sweep. This property can return or be set with a single Profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar. This property returns nothing in the case where the feature is non-parametric.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [profileScaling](SweepFeature_profileScaling.htm) | Gets and sets the sweep profile scaling option. It defaults to SweepProfileScaleOption. This property is only used when a guide rail has been specified.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [sideFaces](SweepFeature_sideFaces.htm) | Property that returns an object that provides access to all of the faces created around the perimeter of the feature. |
| [solidAlignedAxis](SweepFeature_solidAlignedAxis.htm) | Gets and sets the axis to align the solid being swept with. The axis is used when sweeping a solid, and the solid orientation is set to AlignedSolidOrientationType. It can be a sketch line, linear edge, or construction axis. |
| [solidBody](SweepFeature_solidBody.htm) | Gets and sets the BRepBody object to sweep. It must be a solid body. Setting this property results in the type being a single path sweep, and if the profile, guide path, or surface are set, they are set to null.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [solidOrientation](SweepFeature_solidOrientation.htm) | Gets and sets the sweep solid orientation. It defaults to PerpendicularSolidOrientationType. Setting the solid orientation to AlignedSolidOrientationType requires the solid aligned axis to be set. This property is ignored if sweeping a profile.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [solidTwistAxis](SweepFeature_solidTwistAxis.htm) | Gets and sets the twist axis of the solid being swept. The axis is used when sweeping a solid, and the twist angle is set. It can be a sketch line, linear edge, construction axis, or a face that defines an axis (cylinder, cone, torus, etc.). |
| [startFaces](SweepFeature_startFaces.htm) | Property that returns the set of that cap one end of the sweep that are coincident with the sketch plane. In the cases where there aren't any start faces this property will return Nothing. |
| [taperAngle](SweepFeature_taperAngle.htm) | Gets the ModelParameter that defines the taper angle of the sweep feature. The value of the angle can be edited by using the properties on the ModelParameter object to edit the parameter. This property is ignored if sweeping a solid or a guide rail or surface has been specified. |
| [timelineObject](SweepFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |
| [twistAngle](SweepFeature_twistAngle.htm) | Gets the ModelParameter that defines the twist angle of the sweep feature. The value of the angle can be edited by using the properties on the ModelParameter object to edit the parameter. When sweeping a solid setting the twist angle requires the solid twist axis to be set. This property is ignored if a guide rail or surface has been specified. |

## Accessed From

[SweepFeature.createForAssemblyContext](SweepFeature_createForAssemblyContext.htm), [SweepFeature.nativeObject](SweepFeature_nativeObject.htm), [SweepFeatures.add](SweepFeatures_add.htm), [SweepFeatures.item](SweepFeatures_item.htm), [SweepFeatures.itemByName](SweepFeatures_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sweep Feature API Sample](SweepFeatureSample_Sample.htm) | Demonstrates creating a new sweep feature. |
| [Sweep with guide rail Feature API Sample](SweepWithGuideRailFeatureSample_Sample.htm) | Demonstrates creating a new Sweep feature that uses a guide rail along with a profile. |
| [Two Rail Sweep Feature API Sample](TwoRailSweepFeatureSample_Sample.htm) | Demonstrates creating new two rail sweep feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |