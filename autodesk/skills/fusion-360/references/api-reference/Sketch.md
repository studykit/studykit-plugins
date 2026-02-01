# Sketch Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Represents a sketch within a component.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addCenterToCenterSlot](Sketch_addCenterToCenterSlot.htm) | Creates the geometry that represents a slot. Geometric constraints are automatically added to the geometry to maintain the slot shape and optionally, dimensions to control the size can be added. The created geometry and constraints are returned. |
| [classType](Sketch_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Sketch_copy.htm) | Copies the specified sketch entities, applying the specified transform. Any geometric or dimension constraints associated with the entities will automatically be copied, if possible. For example, if there is a horizontal dimension and the transform defines a rotation then it will not be included in the result. This same behavior can be seen when performing a copy/paste operation in the user interface. |
| [createForAssemblyContext](Sketch_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [createSpunProfile](Sketch_createSpunProfile.htm) | Creates sketch geometry that represents the spun profile. The spun profile is the silhouette of the entities as if they were spinning around an axis. The created spun profile is based on the information provided by the SpunProfileInput object. |
| [createSpunProfileInput](Sketch_createSpunProfileInput.htm) | Creates a new SpunProfileInput object that is used to specify the input needed to create a spun profile. |
| [deleteMe](Sketch_deleteMe.htm) | Deletes the sketch. |
| [findConnectedCurves](Sketch_findConnectedCurves.htm) | Finds the sketch curves that are end connected to the input curve. This can be useful for many cases but is especially useful in gathering the input when creating an offset. |
| [importSVG](Sketch_importSVG.htm) | Imports the contents of an SVG file into the active sketch. |
| [include](Sketch_include.htm) | Creates new sketch curves and points that represent the specified entity as sketch geometry. The sketch geometry is not projected but is created in the same location in space as the input geometry. |
| [intersectWithSketchPlane](Sketch_intersectWithSketchPlane.htm) | Intersects the specified entities (BRepBody, BRepFace, BRepEdge, BRepVertex, SketchCurve, ConstructionPoint, ConstructionAxis, and ConstructionPlane) with the sketch plane and creates sketch geometry that represents the intersection. |
| [modelToSketchSpace](Sketch_modelToSketchSpace.htm) | A specified point in model space returns the equivalent point in sketch space. This is sensitive to the assembly context. |
| [move](Sketch_move.htm) | Moves the specified sketch entities using the specified transform. Transform respects any constraints that would normally prohibit the move. |
| [offset](Sketch_offset.htm) | \*\*RETIRED\*\* Creates offset curves for the set of input curves. If the offset distance is not provided, the offset distance is defined by the direction point. |
| [project](Sketch_project.htm) | \*\*RETIRED\*\* This method has been replaced by the project2 method, which supports specifying if the result will be linked or not. |
| [project2](Sketch_project2.htm) | Projects the specified entity or entities onto the X-Y plane of the sketch and returns the created sketch entity(s). |
| [projectCutEdges](Sketch_projectCutEdges.htm) | Intersects the specified body with the sketch plane and creates new curves representing the intersection. |
| [projectToSurface](Sketch_projectToSurface.htm) | Projects the specified set of curves onto the specified set of faces using the specified method of projection. if the projection type is along a vector, then the directionEntity argument must be supplied. if the projectionType is the closest point method, the directionEntity argument is ignored. |
| [redefine](Sketch_redefine.htm) | Changes which plane the sketch is based on. |
| [saveAsDXF](Sketch_saveAsDXF.htm) | \*\*RETIRED\*\* Saves the contents of the sketch to a specified DXF file. |
| [setCenterlineState](Sketch_setCenterlineState.htm) | Method that sets the Centerline state for an array of sketch lines. |
| [setConstructionState](Sketch_setConstructionState.htm) | Method that sets the Construction state for an array of sketch curves. |
| [sketchToModelSpace](Sketch_sketchToModelSpace.htm) | A specified point in sketch space returns the equivalent point in model space. This is sensitive to the assembly context. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [areConstraintsShown](Sketch_areConstraintsShown.htm) | Indicates if the constraints of the sketch are displayed when the sketch is active. |
| [areDimensionsShown](Sketch_areDimensionsShown.htm) | Indicates if the dimensions of the sketch are displayed when the sketch is not active (in sketch edit mode) |
| [arePointsShown](Sketch_arePointsShown.htm) | Indicates if the sketch points in the sketch are displayed. Points that are not connected to any other geometry will continue to be shown. |
| [areProfilesShown](Sketch_areProfilesShown.htm) | Indicates if the profiles of the sketch are displayed |
| [assemblyContext](Sketch_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. |
| [attributes](Sketch_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseOrFormFeature](Sketch_baseOrFormFeature.htm) | This property returns the base or form feature that this sketch is associated with. It returns null in the case where the sketch is parametrically defined and is not related to a base or form feature. It also returns null in a direct modeling design. |
| [boundingBox](Sketch_boundingBox.htm) | Returns the 3D bounding box of the sketch |
| [entityToken](Sketch_entityToken.htm) | Returns a token for the Sketch object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same token. |
| [errorOrWarningMessage](Sketch_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [geometricConstraints](Sketch_geometricConstraints.htm) | Returns the sketch constraints collection associated with this sketch. This provides access to the existing sketch constraints and supports the creation of new sketch constraints. |
| [healthState](Sketch_healthState.htm) | Returns the current health state of this sketch. |
| [isComputeDeferred](Sketch_isComputeDeferred.htm) | This property temporarily turns off sketch computing. It is used to increase the performance as sketch geometry is created and modified. Once the sketch is drawn, this property should be set to false to allow the sketch to recompute. The file does not save this setting and is always false when a file is opened.   There is a side-effect when using this property that can result in the creation of a bad model. This is only a problem when editing an existing sketch used by one or more features. When the sketch is edited with the isComputeDeferred property set to true, the compute of the profiles can sometimes create weird results in the dependent features. There are two easy ways to solve this problem. The first is not to defer the sketch compute. The second is to roll the timeline back to just after the sketch, make whatever changes you want to the sketch with the compute deferred, and then roll the timeline back to its original location. This process mimics the behavior you see in the user interface when you manually edit a sketch where Fusion automatically rolls the timeline back while you're editing the sketch. |
| [isConstructionGeometryShown](Sketch_isConstructionGeometryShown.htm) | Gets and sets whether construction geometry in the sketch is displayed. This provides access to the "Construction Geometries" setting in the "SKETCH PALETTE". |
| [isFullyConstrained](Sketch_isFullyConstrained.htm) | Indicates if this sketch is fully constrained. |
| [isLightBulbOn](Sketch_isLightBulbOn.htm) | Gets and set if the light bulb beside the sketch node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the body is actually visible, just that it should be visible if all of it's parent nodes are also visible. Use the isVisible property to determine if it's actually visible. |
| [isModelSliced](Sketch_isModelSliced.htm) | Gets and sets whether the model is sliced along the sketch plane when this sketch is active. This provides access to the "Slice" setting in the "SKETCH PALETTE". |
| [isParametric](Sketch_isParametric.htm) | Indicates if this sketch is parametric or not. For parametric sketches, you can also get the construction plane or face it is associative to using the ReferencePlane property. |
| [isProjectedGeometryShown](Sketch_isProjectedGeometryShown.htm) | Gets and sets whether projected geometry in the sketch is displayed. This provides access to the "Projected Geometries" setting in the "SKETCH PALETTE". |
| [isValid](Sketch_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](Sketch_isVisible.htm) | Gets if this sketch is currently visible in the graphics window. Use the isLightBulbOn to change if the light bulb beside the sketch node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this body is actually visible or not. |
| [name](Sketch_name.htm) | Gets and sets the name of this sketch as seen in the browser and timeline. |
| [nativeObject](Sketch_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](Sketch_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [origin](Sketch_origin.htm) | Returns the origin point of the sketch in model space. |
| [originPoint](Sketch_originPoint.htm) | Returns the sketch point that was automatically created by projecting the origin construction point into the sketch. |
| [parentComponent](Sketch_parentComponent.htm) | Returns the parent Component. |
| [profiles](Sketch_profiles.htm) | Returns the profiles currently computed for the sketch. |
| [referencePlane](Sketch_referencePlane.htm) | Gets and sets the construction plane or planar face the sketch is associated to. This is only valid when the IsParametric property is True otherwise this returns null and setting the property will fail.   Setting this property is the equivalent of the Redefine command. |
| [revisionId](Sketch_revisionId.htm) | Returns the current revision ID of the sketch. This ID changes any time the sketch is modified in any way. By getting and saving the ID when you create any data that is dependent on the sketch, you can then compare the saved ID with the current ID to determine if the sketch has changed to know if you should update your data. |
| [sketchCurves](Sketch_sketchCurves.htm) | Returns the sketch curves collection associated with this sketch. This provides access to the existing sketch curves which is all geometry in the sketch except for sketch points. It is through this collection that new sketch geometry gets created. |
| [sketchDimensions](Sketch_sketchDimensions.htm) | Returns the sketch dimensions collection associated with this sketch. This provides access to the existing sketch dimensions and supports the creation of new sketch dimensions. |
| [sketchPoints](Sketch_sketchPoints.htm) | Returns the sketch points collection associated with this sketch. This provides access to the existing sketch points and supports the creation of new sketch points. |
| [sketchTexts](Sketch_sketchTexts.htm) | Returns the sketch text collection associated with this sketch. This provides access to existing text and supports the creation of new text. |
| [timelineObject](Sketch_timelineObject.htm) | Returns the timeline object associated with this sketch. |
| [transform](Sketch_transform.htm) | Gets and sets the transform of the sketch with respect to model space. This defines the transform from the parent component space to the sketch space. For example, if you have point coordinates in the space of the parent component and apply this transform it will result in the coordinates of the equivalent position in sketch space. The transform is sensitive to the assembly context.   The position of a parametric sketch cannot be modified since its position is defined by its parametric association to other geometry. As a result this property will fail when called on a parametric sketch. Setting this property is only valid for sketches in a non-parametric design or sketches owned by a base feature. |
| [xDirection](Sketch_xDirection.htm) | Returns the X direction of the sketch as defined in model space. |
| [yDirection](Sketch_yDirection.htm) | Returns the Y direction of the sketch as defined in model space. |

## Accessed From

[BaseFeature.sketches](BaseFeature_sketches.htm), [CircularPatternConstraint.parentSketch](CircularPatternConstraint_parentSketch.htm), [CoincidentConstraint.parentSketch](CoincidentConstraint_parentSketch.htm), [CoincidentToSurfaceConstraint.parentSketch](CoincidentToSurfaceConstraint_parentSketch.htm), [CollinearConstraint.parentSketch](CollinearConstraint_parentSketch.htm), [ConcentricConstraint.parentSketch](ConcentricConstraint_parentSketch.htm), [EqualConstraint.parentSketch](EqualConstraint_parentSketch.htm), [GeometricConstraint.parentSketch](GeometricConstraint_parentSketch.htm), [HorizontalConstraint.parentSketch](HorizontalConstraint_parentSketch.htm), [HorizontalPointsConstraint.parentSketch](HorizontalPointsConstraint_parentSketch.htm), [LineOnPlanarSurfaceConstraint.parentSketch](LineOnPlanarSurfaceConstraint_parentSketch.htm), [LineParallelToPlanarSurfaceConstraint.parentSketch](LineParallelToPlanarSurfaceConstraint_parentSketch.htm), [MidPointConstraint.parentSketch](MidPointConstraint_parentSketch.htm), [OffsetConstraint.parentSketch](OffsetConstraint_parentSketch.htm), [ParallelConstraint.parentSketch](ParallelConstraint_parentSketch.htm), [PerpendicularConstraint.parentSketch](PerpendicularConstraint_parentSketch.htm), [PerpendicularToSurfaceConstraint.parentSketch](PerpendicularToSurfaceConstraint_parentSketch.htm), [PolygonConstraint.parentSketch](PolygonConstraint_parentSketch.htm), [Profile.parentSketch](Profile_parentSketch.htm), [ProfileCurve.parentSketch](ProfileCurve_parentSketch.htm), [RectangularPatternConstraint.parentSketch](RectangularPatternConstraint_parentSketch.htm), [Sketch.createForAssemblyContext](Sketch_createForAssemblyContext.htm), [Sketch.nativeObject](Sketch_nativeObject.htm), [SketchAngularDimension.parentSketch](SketchAngularDimension_parentSketch.htm), [SketchArc.parentSketch](SketchArc_parentSketch.htm), [SketchCircle.parentSketch](SketchCircle_parentSketch.htm), [SketchConcentricCircleDimension.parentSketch](SketchConcentricCircleDimension_parentSketch.htm), [SketchConicCurve.parentSketch](SketchConicCurve_parentSketch.htm), [SketchControlPointSpline.parentSketch](SketchControlPointSpline_parentSketch.htm), [SketchCurve.parentSketch](SketchCurve_parentSketch.htm), [SketchDiameterDimension.parentSketch](SketchDiameterDimension_parentSketch.htm), [SketchDimension.parentSketch](SketchDimension_parentSketch.htm), [SketchDistanceBetweenLineAndPlanarSurfaceDimension.parentSketch](SketchDistanceBetweenLineAndPlanarSurfaceDimension_parentSketch.htm), [SketchDistanceBetweenPointAndSurfaceDimension.parentSketch](SketchDistanceBetweenPointAndSurfaceDimension_parentSketch.htm), [SketchEllipse.parentSketch](SketchEllipse_parentSketch.htm), [SketchEllipseMajorRadiusDimension.parentSketch](SketchEllipseMajorRadiusDimension_parentSketch.htm), [SketchEllipseMinorRadiusDimension.parentSketch](SketchEllipseMinorRadiusDimension_parentSketch.htm), [SketchEllipticalArc.parentSketch](SketchEllipticalArc_parentSketch.htm), [SketchEntity.parentSketch](SketchEntity_parentSketch.htm), [Sketches.add](Sketches_add.htm), [Sketches.addToBaseOrFormFeature](Sketches_addToBaseOrFormFeature.htm), [Sketches.addWithoutEdges](Sketches_addWithoutEdges.htm), [Sketches.item](Sketches_item.htm), [Sketches.itemByName](Sketches_itemByName.htm), [SketchFittedSpline.parentSketch](SketchFittedSpline_parentSketch.htm), [SketchFixedSpline.parentSketch](SketchFixedSpline_parentSketch.htm), [SketchLine.parentSketch](SketchLine_parentSketch.htm), [SketchLinearDiameterDimension.parentSketch](SketchLinearDiameterDimension_parentSketch.htm), [SketchLinearDimension.parentSketch](SketchLinearDimension_parentSketch.htm), [SketchOffsetCurvesDimension.parentSketch](SketchOffsetCurvesDimension_parentSketch.htm), [SketchOffsetDimension.parentSketch](SketchOffsetDimension_parentSketch.htm), [SketchPoint.parentSketch](SketchPoint_parentSketch.htm), [SketchRadialDimension.parentSketch](SketchRadialDimension_parentSketch.htm), [SketchTangentDistanceDimension.parentSketch](SketchTangentDistanceDimension_parentSketch.htm), [SketchText.parentSketch](SketchText_parentSketch.htm), [SmoothConstraint.parentSketch](SmoothConstraint_parentSketch.htm), [SymmetryConstraint.parentSketch](SymmetryConstraint_parentSketch.htm), [TangentConstraint.parentSketch](TangentConstraint_parentSketch.htm), [VerticalConstraint.parentSketch](VerticalConstraint_parentSketch.htm), [VerticalPointsConstraint.parentSketch](VerticalPointsConstraint_parentSketch.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |