# DetailDrawingView Object

Derived from: [DrawingView](../DrawingView/DrawingView.md) Object

## Description

For information on this object, please refer to DrawingView, which provides identical or very similar functionality.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Align](../DetailDrawingView/DetailDrawingView_Align.md) | Method that aligns this view with the input drawing view. The method returns a failure if the view is already aligned. Use the Aligned property to check for this condition and to break existing alignment. |
| [AlignAuxiliary](../DetailDrawingView/DetailDrawingView_AlignAuxiliary.md) | Method that re-aligns an auxiliary view. The method fails if the view is not an auxiliary view. |
| [CopyTo](../DetailDrawingView/DetailDrawingView_CopyTo.md) | Method that copies this drawing view into the specified sheet. The new object is returned. |
| [CreateOriginIndicator](../DetailDrawingView/DetailDrawingView_CreateOriginIndicator.md) | Method that creates the origin indicator for ordinate dimensions and hole tables. The specified input GeometryIntent object must be associated with this drawing view, otherwise this method will fail. |
| [Delete](../DetailDrawingView/DetailDrawingView_Delete.md) | Method that deletes the DrawingView. |
| [DrawingViewToModelSpace](../DetailDrawingView/DetailDrawingView_DrawingViewToModelSpace.md) | Method that takes a 2d coordinate in drawing view space, and returns a Line in model space. Since this method transforms from 2D space to 3D space, there is insufficient information to obtain a 3D model point. Hence, this method returns a Line in the view direction on which the point lies. You may then use the FindUsingRay method to find the point(s) of interest. |
| [DrawingViewToSheetSpace](../DetailDrawingView/DetailDrawingView_DrawingViewToSheetSpace.md) | Method that takes a 2d coordinate in drawing view space, and returns a Point2d containing the coordinates of the point in sheet space. |
| [GetAutomatedCenterlineSettings](../DetailDrawingView/DetailDrawingView_GetAutomatedCenterlineSettings.md) | Method that returns the settings that define how automatic center lines and center marks are to be calculated for this view. |
| [GetComponentLineColor](../DetailDrawingView/DetailDrawingView_GetComponentLineColor.md) | Method that gets color of a component in drawing view. |
| [GetHiddenLinesStatus](../DetailDrawingView/DetailDrawingView_GetHiddenLinesStatus.md) | Method that gets the hidden lines status of a component in the drawing view. |
| [GetIncludeStatus](../DetailDrawingView/DetailDrawingView_GetIncludeStatus.md) | Method that gets the include status of the input object in the drawing view. |
| [GetReferenceKey](../DetailDrawingView/DetailDrawingView_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetVisibility](../DetailDrawingView/DetailDrawingView_GetVisibility.md) | Method that gets the visibility of the input object in the drawing view. This returns error if the input object has partial visibility status. |
| [GetWeldmentState](../DetailDrawingView/DetailDrawingView_GetWeldmentState.md) | Method that gets the weldment option for the drawing view. The method returns a failure if the referenced model does not contain weldments. |
| [InsertInModelSpace](../DetailDrawingView/DetailDrawingView_InsertInModelSpace.md) | Inserts the view geometry into model space only if the drawing lives in an Inventor DWG file. |
| [ModelToDrawingViewSpace](../DetailDrawingView/DetailDrawingView_ModelToDrawingViewSpace.md) | Method that takes a 3d coordinate in model space, and returns a Point2d object containing the coordinate point in drawing view space. |
| [ModelToSheetSpace](../DetailDrawingView/DetailDrawingView_ModelToSheetSpace.md) | Method that takes a 3d coordinate in model space, and returns a Point2d object containing the coordinate point in sheet space. |
| [MoveTo](../DetailDrawingView/DetailDrawingView_MoveTo.md) | Method that moves this drawing view into the specified sheet. The moved object is returned. |
| [RotateByAngle](../DetailDrawingView/DetailDrawingView_RotateByAngle.md) | Method that rotates the drawing view by the specified angle. |
| [SetActiveModelState](../DetailDrawingView/DetailDrawingView_SetActiveModelState.md) | Method that sets the active model state for a drawing view. In this method users can also decide to update the PartsList objects which use the same model state as the drawing view. This method fails for drawing views where the model is unresolved. |
| [SetAutomatedCenterlineSettings](../DetailDrawingView/DetailDrawingView_SetAutomatedCenterlineSettings.md) | Method that sets the automatic centerline and center mark settings for this view and creates the centerlines and center marks defined by the settings. The centerlines and center marks that were created are returned. |
| [SetComponentLineColor](../DetailDrawingView/DetailDrawingView_SetComponentLineColor.md) | Method that sets color for a component in the drawing view. |
| [SetDesignViewRepresentation](../DetailDrawingView/DetailDrawingView_SetDesignViewRepresentation.md) | Method that sets a design view representation for a drawing view of an assembly. This method fails for drawing views of parts and presentations and in the case where the model (assembly) is unresolved. |
| [SetHiddenLinesStatus](../DetailDrawingView/DetailDrawingView_SetHiddenLinesStatus.md) | Method that sets the hidden lines status of a component in the drawing view. |
| [SetIncludeStatus](../DetailDrawingView/DetailDrawingView_SetIncludeStatus.md) | Method that sets the include status of the input object in the drawing view. This method automatically makes the object visible as well. After an object has been included, its visibility can be controlled using the GetVisibility and SetVisibility methods. |
| [SetVisibility](../DetailDrawingView/DetailDrawingView_SetVisibility.md) | Method that sets the visibility of the input object in the drawing view. |
| [SetWeldmentState](../DetailDrawingView/DetailDrawingView_SetWeldmentState.md) | Method that sets the weldment option for the drawing view. The method returns a failure if the referenced model does not contain weldments. |
| [SheetToDrawingViewSpace](../DetailDrawingView/DetailDrawingView_SheetToDrawingViewSpace.md) | Method that takes a 2d coordinate in sheet space, and returns a Point2d object containing the coordinate point in drawing view space. |
| [SheetToModelSpace](../DetailDrawingView/DetailDrawingView_SheetToModelSpace.md) | Method that takes a 2d coordinate in sheet space, and returns a Line in model space. Since this method transforms from 2D space to 3D space, there is insufficient information to obtain a 3D model point. Hence, this method returns a Line in the view direction on which the point lies. You may then use the FindUsingRay method to find the point(s) of interest. |
| [ShowHiddenAnnotations](../DetailDrawingView/DetailDrawingView_ShowHiddenAnnotations.md) | Method that displays all the annotations hidden by the user. |
| [ShowHiddenCurves](../DetailDrawingView/DetailDrawingView_ShowHiddenCurves.md) | Method that displays all the curves explicitly hidden by the user. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveMemberName](../DetailDrawingView/DetailDrawingView_ActiveMemberName.md) | Gets and sets the name of the active member for a drawing view of an iPart or an iAssembly. |
| [ActiveModelState](../DetailDrawingView/DetailDrawingView_ActiveModelState.md) | Read-only property that gets the name of the active model state for a drawing view. This property returns a null string for drawing views of presentations and in the case where the model is unresolved. |
| [ActivePositionalRepresentation](../DetailDrawingView/DetailDrawingView_ActivePositionalRepresentation.md) | Gets and sets the name of the active Positional Representation for a drawing view of an assembly. |
| [ActivePresentationView](../DetailDrawingView/DetailDrawingView_ActivePresentationView.md) | Property that returns the name of the active Presentation (Exploded) View for a drawing view of a presentation. |
| [Aligned](../DetailDrawingView/DetailDrawingView_Aligned.md) | Gets and sets whether the view is aligned with another view. |
| [AttachPoint](../DetailDrawingView/DetailDrawingView_AttachPoint.md) | Property that gets and sets geometry to attach the view to. Use Sheet.CreateGeometryIntent method to create a new GeometryIntent object. This property can be set to Nothing to un-attach the view from a geometry. |
| [AttributeSets](../DetailDrawingView/DetailDrawingView_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AuxiliaryOrientationEdge](../DetailDrawingView/DetailDrawingView_AuxiliaryOrientationEdge.md) | Property that returns drawing curve that the auxiliary view is aligned to. This property returns Nothing if this is not an auxiliary view or if the orientation edge (drawing curve) has been removed from the parent view during a subsequent update. |
| [BitmapAvailable](../DetailDrawingView/DetailDrawingView_BitmapAvailable.md) | Property that returns if this view's graphics are also available as a bitmap as well. If a bitmap exists it can be retrieved using the DataIO object. This is only applicable within Apprentice. |
| [BoundaryLayer](../DetailDrawingView/DetailDrawingView_BoundaryLayer.md) | Property that gets and sets the layer associated with the boundary geometry. |
| [BreakOperations](../DetailDrawingView/DetailDrawingView_BreakOperations.md) | Property that returns the BreakOperations object containing information about all the break operations applied to this view as well as methods to add breaks. Both local as well as inherited break operations are returned in the collection. |
| [BreakOutOperations](../DetailDrawingView/DetailDrawingView_BreakOutOperations.md) | Property that returns the BreakOutOperations object containing information about all the break out operations applied to this view as well as methods to add break outs. Only local break out operations are returned. |
| [Camera](../DetailDrawingView/DetailDrawingView_Camera.md) | Property that returns a Camera object that defines the orientation of the model within the view. |
| [Center](../DetailDrawingView/DetailDrawingView_Center.md) | Gets and sets the display center point of the drawing view on the owning sheet. |
| [CircularFence](../DetailDrawingView/DetailDrawingView_CircularFence.md) | Gets whether the detail view uses a circular fence or a rectangular fence. |
| [ClientGraphicsCollection](../DetailDrawingView/DetailDrawingView_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [CropOperations](../DetailDrawingView/DetailDrawingView_CropOperations.md) | Read-only property that returns the CropOperations object containing information about all the crop operations applied to this view as well as methods to add crops. |
| [DataIO](../DetailDrawingView/DetailDrawingView_DataIO.md) | Property that returns the associated DataIO object. This can be used in Apprentice to obtain an associated bitmap, if it exists. |
| [DesignViewAssociative](../DetailDrawingView/DetailDrawingView_DesignViewAssociative.md) | Read-only property that gets whether the DesignViewRepresentation for a drawing view of a model is associative or not. |
| [DesignViewRepresentation](../DetailDrawingView/DetailDrawingView_DesignViewRepresentation.md) | Read-only property that returns the name of the Design View Representation for a drawing view of a model. |
| [DisplayBendExtents](../DetailDrawingView/DetailDrawingView_DisplayBendExtents.md) | Gets and sets whether to display sheet metal bend extents on the drawing view. |
| [DisplayConnectionLine](../DetailDrawingView/DetailDrawingView_DisplayConnectionLine.md) | Property that gets and sets whether to display the line between the detail view fence and the full boundary. This property can be set to True only if the IsBreakLineSmooth and DisplayFullBoundary properties are set to True. |
| [DisplayDefinitionInBase](../DetailDrawingView/DetailDrawingView_DisplayDefinitionInBase.md) | Gets and sets whether to display detail circles, section lines and the associated text in the base view. |
| [DisplayForeshortenedTangentEdges](../DetailDrawingView/DetailDrawingView_DisplayForeshortenedTangentEdges.md) | Gets and sets whether to display shortened tangent edges in order to distinguish them from visible edges. |
| [DisplayFullBoundary](../DetailDrawingView/DetailDrawingView_DisplayFullBoundary.md) | Property that gets and sets whether to display full boundary of the detail view. This property can be set to True only if the IsBreakLineSmooth property is set to True. |
| [DisplayHatching](../DetailDrawingView/DetailDrawingView_DisplayHatching.md) | Gets and sets whether to display hatches for section and slice views. |
| [DisplayInterferenceEdges](../DetailDrawingView/DetailDrawingView_DisplayInterferenceEdges.md) | Gets and sets whether to display both hidden edges that are excluded due to an interference condition (press, or interference fit conditions, threaded fasteners in tapped holes where the hole feature is modeled with the minor diameter). |
| [DisplayTangentEdges](../DetailDrawingView/DetailDrawingView_DisplayTangentEdges.md) | Read-write property that gets and sets whether to display the tangent edges on the drawing view. |
| [DisplayThreadFeatures](../DetailDrawingView/DetailDrawingView_DisplayThreadFeatures.md) | Gets and sets whether to display thread features on the drawing view. |
| [DisplayTrails](../DetailDrawingView/DetailDrawingView_DisplayTrails.md) | Gets and sets whether to display trails. |
| [DrawingCurves](../DetailDrawingView/DetailDrawingView_DrawingCurves.md) | Property that returns all the drawing curves within the drawing view optionally filtered to the input model object. This property returns Nothing for draft views.iew object represents a drawing view on a sheet. |
| [DrawingViewEvents](../DetailDrawingView/DetailDrawingView_DrawingViewEvents.md) | Property that returns the object, which provides event notifcation. For example, view updates. |
| [DrawingViewToModelTransform](../DetailDrawingView/DetailDrawingView_DrawingViewToModelTransform.md) | Property that returns the transformation from drawing view coordinate space to the model space. |
| [DrawingViewToSheetTransform](../DetailDrawingView/DetailDrawingView_DrawingViewToSheetTransform.md) | Property that returns the transformation from drawing view coordinate space to the sheet space. |
| [FenceCenter](../DetailDrawingView/DetailDrawingView_FenceCenter.md) | Property that gets and sets the center of the fence. Applies to both circular and rectangular fence types. Setting this property will fail if the view is attached to geometry (i.e. the AttachPoint property returns an object). |
| [FenceCornerOne](../DetailDrawingView/DetailDrawingView_FenceCornerOne.md) | Property that gets and sets the first corner of the rectangular fence. This property returns Nothing and cannot be set if the fence type is circular. |
| [FenceCornerTwo](../DetailDrawingView/DetailDrawingView_FenceCornerTwo.md) | Property that gets and sets the second corner of the rectangular fence. This property returns Nothing and cannot be set if the fence type is circular. |
| [FenceRadius](../DetailDrawingView/DetailDrawingView_FenceRadius.md) | Property that gets and sets the radius of the circular fence. This property fails if the fence type is rectangular. |
| [GeneralDimensionType](../DetailDrawingView/DetailDrawingView_GeneralDimensionType.md) | Read-write property that indicates the type of dimension. |
| [GraphicsDataSetsCollection](../DetailDrawingView/DetailDrawingView_GraphicsDataSetsCollection.md) | Property that returns the object for the drawing view. |
| [HasOriginIndicator](../DetailDrawingView/DetailDrawingView_HasOriginIndicator.md) | Property that specifies whether the origin indicator for ordinate dimensions and hole tables has been created. |
| [HatchRegions](../DetailDrawingView/DetailDrawingView_HatchRegions.md) | Read-only property that returns the DrawingViewHatchRegions collection object. |
| [Height](../DetailDrawingView/DetailDrawingView_Height.md) | Property that specifies the height of the drawing view. The view height cannot be set but is defined by the contents of the view |
| [HiddenLineCalculationForAllBodies](../DetailDrawingView/DetailDrawingView_HiddenLineCalculationForAllBodies.md) | Read-write property that gets and sets whether the hidden line are calculated for all bodies or reference data separately. |
| [Include3DAnnotations](../DetailDrawingView/DetailDrawingView_Include3DAnnotations.md) | Read-write property that gets and sets whether to include the 3D annotations. |
| [IncludeMeshBodies](../DetailDrawingView/DetailDrawingView_IncludeMeshBodies.md) | Read-write property that gets and sets whether to include the mesh bodies. |
| [IncludeSurfaceBodies](../DetailDrawingView/DetailDrawingView_IncludeSurfaceBodies.md) | Read-write property that gets and sets whether to include the work surfaces. |
| [InheritBreak](../DetailDrawingView/DetailDrawingView_InheritBreak.md) | Gets and sets whether the view should inherit the corresponding break from the parent view. |
| [InheritBreakOut](../DetailDrawingView/DetailDrawingView_InheritBreakOut.md) | Gets and sets whether the view should inherit the corresponding break out from the parent view. |
| [InheritSection](../DetailDrawingView/DetailDrawingView_InheritSection.md) | Gets and sets whether the view should inherit the corresponding section cut from the parent view. |
| [InheritSlice](../DetailDrawingView/DetailDrawingView_InheritSlice.md) | Gets and sets whether the view should inherit the corresponding slice cut from the parent view. |
| [IsBreakLineSmooth](../DetailDrawingView/DetailDrawingView_IsBreakLineSmooth.md) | Property that gets and sets whether the cut shape of the fence is smooth or jogged. |
| [IsFlatPatternView](../DetailDrawingView/DetailDrawingView_IsFlatPatternView.md) | Gets whether the drawing view is of a sheet metal flat pattern. |
| [IsRasterView](../DetailDrawingView/DetailDrawingView_IsRasterView.md) | Read-write property that gets and sets whether the drawing view is raster view or not. |
| [IsTextPropertySource](../DetailDrawingView/DetailDrawingView_IsTextPropertySource.md) | Read-write property that gets and sets whether the drawing view is specified as the text property source.This is applicable only when the drawing view is a base view. |
| [IsUpdateComplete](../DetailDrawingView/DetailDrawingView_IsUpdateComplete.md) | Indicates if the view has finished updating. |
| [Label](../DetailDrawingView/DetailDrawingView_Label.md) | Property that returns the DrawingViewLabel object. |
| [Left](../DetailDrawingView/DetailDrawingView_Left.md) | Property that returns the position of the left edge of the drawing view. |
| [Margin](../DetailDrawingView/DetailDrawingView_Margin.md) | Read-write property that gets and sets the amount of area outside the normal view boundary that the view boundary extends. |
| [ModelToDrawingViewTransform](../DetailDrawingView/DetailDrawingView_ModelToDrawingViewTransform.md) | Property that returns the transformation from model space to the drawing view coordinate space. |
| [ModelToSheetTransform](../DetailDrawingView/DetailDrawingView_ModelToSheetTransform.md) | Property that returns the transformation from model space to the sheet coordinate space. |
| [Name](../DetailDrawingView/DetailDrawingView_Name.md) | Gets or sets the name of this View. |
| [OriginIndicator](../DetailDrawingView/DetailDrawingView_OriginIndicator.md) | Property that gets the origin indicator for ordinate dimensions and hole tables. |
| [Parent](../DetailDrawingView/DetailDrawingView_Parent.md) | Property returning the parent Sheet object. |
| [ParentView](../DetailDrawingView/DetailDrawingView_ParentView.md) | Property that returns the parent . This property returns Nothing in the case where no parent view exists. |
| [Position](../DetailDrawingView/DetailDrawingView_Position.md) | Gets and sets the point used to position the drawing view on the sheet. |
| [PresentationViewAssociative](../DetailDrawingView/DetailDrawingView_PresentationViewAssociative.md) | Gets and sets whether to associate the drawing view to the referenced presentation view. |
| [ReferenceDataDisplayStyle](../DetailDrawingView/DetailDrawingView_ReferenceDataDisplayStyle.md) | Read-write property that gets and sets the reference data display style. |
| [ReferencedDocumentDescriptor](../DetailDrawingView/DetailDrawingView_ReferencedDocumentDescriptor.md) | Property that returns the model document referenced by this view. |
| [RevisionClouds](../DetailDrawingView/DetailDrawingView_RevisionClouds.md) | Returns the collection of revision clouds on this drawing view. |
| [Rotation](../DetailDrawingView/DetailDrawingView_Rotation.md) | Read-write property that gets and sets the absolute rotation angle of the drawing view in radians. The value can either be positive (counter-clockwise rotation) or negative (clockwise rotation). |
| [Scale](../DetailDrawingView/DetailDrawingView_Scale.md) | Gets or sets the Model-to-PaperSpace scale of this particular Drawing View. |
| [ScaleFromBase](../DetailDrawingView/DetailDrawingView_ScaleFromBase.md) | Gets and sets whether the scale of the view derives from the parent view or not. |
| [ScaleString](../DetailDrawingView/DetailDrawingView_ScaleString.md) | Gets or sets the Model-to-PaperSpace scale in string format of this particular Drawing View. |
| [SheetToDrawingViewTransform](../DetailDrawingView/DetailDrawingView_SheetToDrawingViewTransform.md) | Property that returns the transformation from sheet space to the drawing view coordinate space. |
| [SheetToModelTransform](../DetailDrawingView/DetailDrawingView_SheetToModelTransform.md) | Property that returns the transformation from sheet coordinate space to the model space. |
| [ShowLabel](../DetailDrawingView/DetailDrawingView_ShowLabel.md) | Gets and sets whether to show the label of the drawing view on the sheet. |
| [ShowTrails](../DetailDrawingView/DetailDrawingView_ShowTrails.md) | Gets and set whether to show the trails or not for a drawing view of a presentation. |
| [Sketches](../DetailDrawingView/DetailDrawingView_Sketches.md) | Property that returns the DrawingSketches collection object for the sheet. This object provides access to all of the sketches that have been created on the sheet and provides functionality to create new sketches. |
| [StandardPartsSectionBehavior](../DetailDrawingView/DetailDrawingView_StandardPartsSectionBehavior.md) | Gets and sets the sectioning behavior for standard parts in drawing views of assemblies. |
| [Suppressed](../DetailDrawingView/DetailDrawingView_Suppressed.md) | Gets and sets whether this drawing view is suppressed or not. |
| [Top](../DetailDrawingView/DetailDrawingView_Top.md) | Property that specifies the position of the top edge of the drawing view. |
| [Type](../DetailDrawingView/DetailDrawingView_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../DetailDrawingView/DetailDrawingView_UpToDate.md) | Property that returns whether the drawing view is up to date with respect to the model. |
| [ViewAnnotation](../DetailDrawingView/DetailDrawingView_ViewAnnotation.md) | Read-only property that returns the drawing view annotation object. |
| [ViewJustification](../DetailDrawingView/DetailDrawingView_ViewJustification.md) | Gets and sets the view justification. |
| [ViewOrientationFromBase](../DetailDrawingView/DetailDrawingView_ViewOrientationFromBase.md) | Gets and sets whether the view should inherit the orientation from the base view. |
| [ViewStyle](../DetailDrawingView/DetailDrawingView_ViewStyle.md) | Gets and sets the drawing view style. |
| [ViewType](../DetailDrawingView/DetailDrawingView_ViewType.md) | Property returning an DrawingViewTypeEnum constant indicating the type of view. |
| [Width](../DetailDrawingView/DetailDrawingView_Width.md) | Property that specifies the width of the drawing view. The view width cannot be set but is defined by the contents of the view. |

## Accessed From

[DrawingViews.AddDetailView](../DrawingViews/DrawingViews_AddDetailView.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |