# DrawingView Object

## Description

The DrawingView object represents a drawing view on a sheet. It allows access to information about drawing views. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Align](../DrawingView/DrawingView_Align.md) | Method that aligns this view with the input drawing view. The method returns a failure if the view is already aligned. Use the Aligned property to check for this condition and to break existing alignment. |
| [AlignAuxiliary](../DrawingView/DrawingView_AlignAuxiliary.md) | Method that re-aligns an auxiliary view. The method fails if the view is not an auxiliary view. |
| [CopyTo](../DrawingView/DrawingView_CopyTo.md) | Method that copies this drawing view into the specified sheet. The new object is returned. |
| [CreateOriginIndicator](../DrawingView/DrawingView_CreateOriginIndicator.md) | Method that creates the origin indicator for ordinate dimensions and hole tables. The specified input GeometryIntent object must be associated with this drawing view, otherwise this method will fail. |
| [Delete](../DrawingView/DrawingView_Delete.md) | Method that deletes the DrawingView. |
| [DrawingViewToModelSpace](../DrawingView/DrawingView_DrawingViewToModelSpace.md) | Method that takes a 2d coordinate in drawing view space, and returns a Line in model space. Since this method transforms from 2D space to 3D space, there is insufficient information to obtain a 3D model point. Hence, this method returns a Line in the view direction on which the point lies. You may then use the FindUsingRay method to find the point(s) of interest. |
| [DrawingViewToSheetSpace](../DrawingView/DrawingView_DrawingViewToSheetSpace.md) | Method that takes a 2d coordinate in drawing view space, and returns a Point2d containing the coordinates of the point in sheet space. |
| [GetAutomatedCenterlineSettings](../DrawingView/DrawingView_GetAutomatedCenterlineSettings.md) | Method that returns the settings that define how automatic center lines and center marks are to be calculated for this view. |
| [GetComponentLineColor](../DrawingView/DrawingView_GetComponentLineColor.md) | Method that gets color of a component in drawing view. |
| [GetHiddenLinesStatus](../DrawingView/DrawingView_GetHiddenLinesStatus.md) | Method that gets the hidden lines status of a component in the drawing view. |
| [GetIncludeStatus](../DrawingView/DrawingView_GetIncludeStatus.md) | Method that gets the include status of the input object in the drawing view. |
| [GetReferenceKey](../DrawingView/DrawingView_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetVisibility](../DrawingView/DrawingView_GetVisibility.md) | Method that gets the visibility of the input object in the drawing view. This returns error if the input object has partial visibility status. |
| [GetWeldmentState](../DrawingView/DrawingView_GetWeldmentState.md) | Method that gets the weldment option for the drawing view. The method returns a failure if the referenced model does not contain weldments. |
| [InsertInModelSpace](../DrawingView/DrawingView_InsertInModelSpace.md) | Inserts the view geometry into model space only if the drawing lives in an Inventor DWG file. |
| [ModelToDrawingViewSpace](../DrawingView/DrawingView_ModelToDrawingViewSpace.md) | Method that takes a 3d coordinate in model space, and returns a Point2d object containing the coordinate point in drawing view space. |
| [ModelToSheetSpace](../DrawingView/DrawingView_ModelToSheetSpace.md) | Method that takes a 3d coordinate in model space, and returns a Point2d object containing the coordinate point in sheet space. |
| [MoveTo](../DrawingView/DrawingView_MoveTo.md) | Method that moves this drawing view into the specified sheet. The moved object is returned. |
| [RotateByAngle](../DrawingView/DrawingView_RotateByAngle.md) | Method that rotates the drawing view by the specified angle. |
| [SetActiveModelState](../DrawingView/DrawingView_SetActiveModelState.md) | Method that sets the active model state for a drawing view. In this method users can also decide to update the PartsList objects which use the same model state as the drawing view. This method fails for drawing views where the model is unresolved. |
| [SetAutomatedCenterlineSettings](../DrawingView/DrawingView_SetAutomatedCenterlineSettings.md) | Method that sets the automatic centerline and center mark settings for this view and creates the centerlines and center marks defined by the settings. The centerlines and center marks that were created are returned. |
| [SetComponentLineColor](../DrawingView/DrawingView_SetComponentLineColor.md) | Method that sets color for a component in the drawing view. |
| [SetDesignViewRepresentation](../DrawingView/DrawingView_SetDesignViewRepresentation.md) | Method that sets a design view representation for a drawing view of an assembly. This method fails for drawing views of parts and presentations and in the case where the model (assembly) is unresolved. |
| [SetHiddenLinesStatus](../DrawingView/DrawingView_SetHiddenLinesStatus.md) | Method that sets the hidden lines status of a component in the drawing view. |
| [SetIncludeStatus](../DrawingView/DrawingView_SetIncludeStatus.md) | Method that sets the include status of the input object in the drawing view. This method automatically makes the object visible as well. After an object has been included, its visibility can be controlled using the GetVisibility and SetVisibility methods. |
| [SetVisibility](../DrawingView/DrawingView_SetVisibility.md) | Method that sets the visibility of the input object in the drawing view. |
| [SetWeldmentState](../DrawingView/DrawingView_SetWeldmentState.md) | Method that sets the weldment option for the drawing view. The method returns a failure if the referenced model does not contain weldments. |
| [SheetToDrawingViewSpace](../DrawingView/DrawingView_SheetToDrawingViewSpace.md) | Method that takes a 2d coordinate in sheet space, and returns a Point2d object containing the coordinate point in drawing view space. |
| [SheetToModelSpace](../DrawingView/DrawingView_SheetToModelSpace.md) | Method that takes a 2d coordinate in sheet space, and returns a Line in model space. Since this method transforms from 2D space to 3D space, there is insufficient information to obtain a 3D model point. Hence, this method returns a Line in the view direction on which the point lies. You may then use the FindUsingRay method to find the point(s) of interest. |
| [ShowHiddenAnnotations](../DrawingView/DrawingView_ShowHiddenAnnotations.md) | Method that displays all the annotations hidden by the user. |
| [ShowHiddenCurves](../DrawingView/DrawingView_ShowHiddenCurves.md) | Method that displays all the curves explicitly hidden by the user. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveMemberName](../DrawingView/DrawingView_ActiveMemberName.md) | Gets and sets the name of the active member for a drawing view of an iPart or an iAssembly. |
| [ActiveModelState](../DrawingView/DrawingView_ActiveModelState.md) | Read-only property that gets the name of the active model state for a drawing view. This property returns a null string for drawing views of presentations and in the case where the model is unresolved. |
| [ActivePositionalRepresentation](../DrawingView/DrawingView_ActivePositionalRepresentation.md) | Gets and sets the name of the active Positional Representation for a drawing view of an assembly. |
| [ActivePresentationView](../DrawingView/DrawingView_ActivePresentationView.md) | Property that returns the name of the active Presentation (Exploded) View for a drawing view of a presentation. |
| [Aligned](../DrawingView/DrawingView_Aligned.md) | Gets and sets whether the view is aligned with another view. |
| [AttributeSets](../DrawingView/DrawingView_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AuxiliaryOrientationEdge](../DrawingView/DrawingView_AuxiliaryOrientationEdge.md) | Property that returns drawing curve that the auxiliary view is aligned to. This property returns Nothing if this is not an auxiliary view or if the orientation edge (drawing curve) has been removed from the parent view during a subsequent update. |
| [BitmapAvailable](../DrawingView/DrawingView_BitmapAvailable.md) | Property that returns if this view's graphics are also available as a bitmap as well. If a bitmap exists it can be retrieved using the DataIO object. This is only applicable within Apprentice. |
| [BreakOperations](../DrawingView/DrawingView_BreakOperations.md) | Property that returns the BreakOperations object containing information about all the break operations applied to this view as well as methods to add breaks. Both local as well as inherited break operations are returned in the collection. |
| [BreakOutOperations](../DrawingView/DrawingView_BreakOutOperations.md) | Property that returns the BreakOutOperations object containing information about all the break out operations applied to this view as well as methods to add break outs. Only local break out operations are returned. |
| [Camera](../DrawingView/DrawingView_Camera.md) | Property that returns a Camera object that defines the orientation of the model within the view. |
| [Center](../DrawingView/DrawingView_Center.md) | Gets and sets the display center point of the drawing view on the owning sheet. |
| [ClientGraphicsCollection](../DrawingView/DrawingView_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. |
| [CropOperations](../DrawingView/DrawingView_CropOperations.md) | Read-only property that returns the CropOperations object containing information about all the crop operations applied to this view as well as methods to add crops. |
| [DataIO](../DrawingView/DrawingView_DataIO.md) | Property that returns the associated DataIO object. This can be used in Apprentice to obtain an associated bitmap, if it exists. |
| [DesignViewAssociative](../DrawingView/DrawingView_DesignViewAssociative.md) | Read-only property that gets whether the DesignViewRepresentation for a drawing view of a model is associative or not. |
| [DesignViewRepresentation](../DrawingView/DrawingView_DesignViewRepresentation.md) | Read-only property that returns the name of the Design View Representation for a drawing view of a model. |
| [DisplayBendExtents](../DrawingView/DrawingView_DisplayBendExtents.md) | Gets and sets whether to display sheet metal bend extents on the drawing view. |
| [DisplayDefinitionInBase](../DrawingView/DrawingView_DisplayDefinitionInBase.md) | Gets and sets whether to display detail circles, section lines and the associated text in the base view. |
| [DisplayForeshortenedTangentEdges](../DrawingView/DrawingView_DisplayForeshortenedTangentEdges.md) | Gets and sets whether to display shortened tangent edges in order to distinguish them from visible edges. |
| [DisplayHatching](../DrawingView/DrawingView_DisplayHatching.md) | Gets and sets whether to display hatches for section and slice views. |
| [DisplayInterferenceEdges](../DrawingView/DrawingView_DisplayInterferenceEdges.md) | Gets and sets whether to display both hidden edges that are excluded due to an interference condition (press, or interference fit conditions, threaded fasteners in tapped holes where the hole feature is modeled with the minor diameter). |
| [DisplayTangentEdges](../DrawingView/DrawingView_DisplayTangentEdges.md) | Read-write property that gets and sets whether to display the tangent edges on the drawing view. |
| [DisplayThreadFeatures](../DrawingView/DrawingView_DisplayThreadFeatures.md) | Gets and sets whether to display thread features on the drawing view. |
| [DisplayTrails](../DrawingView/DrawingView_DisplayTrails.md) | Gets and sets whether to display trails. |
| [DrawingCurves](../DrawingView/DrawingView_DrawingCurves.md) | Property that returns all the drawing curves within the drawing view optionally filtered to the input model object. This property returns Nothing for draft views.iew object represents a drawing view on a sheet. |
| [DrawingViewEvents](../DrawingView/DrawingView_DrawingViewEvents.md) | Property that returns the object, which provides event notifcation. For example, view updates. |
| [DrawingViewToModelTransform](../DrawingView/DrawingView_DrawingViewToModelTransform.md) | Property that returns the transformation from drawing view coordinate space to the model space. |
| [DrawingViewToSheetTransform](../DrawingView/DrawingView_DrawingViewToSheetTransform.md) | Property that returns the transformation from drawing view coordinate space to the sheet space. |
| [GeneralDimensionType](../DrawingView/DrawingView_GeneralDimensionType.md) | Read-write property that indicates the type of dimension. |
| [GraphicsDataSetsCollection](../DrawingView/DrawingView_GraphicsDataSetsCollection.md) | Property that returns the object for the drawing view. |
| [HasOriginIndicator](../DrawingView/DrawingView_HasOriginIndicator.md) | Property that specifies whether the origin indicator for ordinate dimensions and hole tables has been created. |
| [HatchRegions](../DrawingView/DrawingView_HatchRegions.md) | Read-only property that returns the DrawingViewHatchRegions collection object. |
| [Height](../DrawingView/DrawingView_Height.md) | Property that specifies the height of the drawing view. The view height cannot be set but is defined by the contents of the view |
| [HiddenLineCalculationForAllBodies](../DrawingView/DrawingView_HiddenLineCalculationForAllBodies.md) | Read-write property that gets and sets whether the hidden line are calculated for all bodies or reference data separately. |
| [Include3DAnnotations](../DrawingView/DrawingView_Include3DAnnotations.md) | Read-write property that gets and sets whether to include the 3D annotations. |
| [IncludeMeshBodies](../DrawingView/DrawingView_IncludeMeshBodies.md) | Read-write property that gets and sets whether to include the mesh bodies. |
| [IncludeSurfaceBodies](../DrawingView/DrawingView_IncludeSurfaceBodies.md) | Read-write property that gets and sets whether to include the work surfaces. |
| [InheritBreak](../DrawingView/DrawingView_InheritBreak.md) | Gets and sets whether the view should inherit the corresponding break from the parent view. |
| [InheritBreakOut](../DrawingView/DrawingView_InheritBreakOut.md) | Gets and sets whether the view should inherit the corresponding break out from the parent view. |
| [InheritSection](../DrawingView/DrawingView_InheritSection.md) | Gets and sets whether the view should inherit the corresponding section cut from the parent view. |
| [InheritSlice](../DrawingView/DrawingView_InheritSlice.md) | Gets and sets whether the view should inherit the corresponding slice cut from the parent view. |
| [IsFlatPatternView](../DrawingView/DrawingView_IsFlatPatternView.md) | Gets whether the drawing view is of a sheet metal flat pattern. |
| [IsRasterView](../DrawingView/DrawingView_IsRasterView.md) | Read-write property that gets and sets whether the drawing view is raster view or not. |
| [IsTextPropertySource](../DrawingView/DrawingView_IsTextPropertySource.md) | Read-write property that gets and sets whether the drawing view is specified as the text property source.This is applicable only when the drawing view is a base view. |
| [IsUpdateComplete](../DrawingView/DrawingView_IsUpdateComplete.md) | Indicates if the view has finished updating. |
| [Label](../DrawingView/DrawingView_Label.md) | Property that returns the DrawingViewLabel object. |
| [Left](../DrawingView/DrawingView_Left.md) | Property that returns the position of the left edge of the drawing view. |
| [Margin](../DrawingView/DrawingView_Margin.md) | Read-write property that gets and sets the amount of area outside the normal view boundary that the view boundary extends. |
| [ModelToDrawingViewTransform](../DrawingView/DrawingView_ModelToDrawingViewTransform.md) | Property that returns the transformation from model space to the drawing view coordinate space. |
| [ModelToSheetTransform](../DrawingView/DrawingView_ModelToSheetTransform.md) | Property that returns the transformation from model space to the sheet coordinate space. |
| [Name](../DrawingView/DrawingView_Name.md) | Gets or sets the name of this View. |
| [OriginIndicator](../DrawingView/DrawingView_OriginIndicator.md) | Property that gets the origin indicator for ordinate dimensions and hole tables. |
| [Parent](../DrawingView/DrawingView_Parent.md) | Property returning the parent Sheet object. |
| [ParentView](../DrawingView/DrawingView_ParentView.md) | Property that returns the parent . This property returns Nothing in the case where no parent view exists. |
| [Position](../DrawingView/DrawingView_Position.md) | Gets and sets the point used to position the drawing view on the sheet. |
| [PresentationViewAssociative](../DrawingView/DrawingView_PresentationViewAssociative.md) | Gets and sets whether to associate the drawing view to the referenced presentation view. |
| [ReferenceDataDisplayStyle](../DrawingView/DrawingView_ReferenceDataDisplayStyle.md) | Read-write property that gets and sets the reference data display style. |
| [ReferencedDocumentDescriptor](../DrawingView/DrawingView_ReferencedDocumentDescriptor.md) | Property that returns the model document referenced by this view. |
| [RevisionClouds](../DrawingView/DrawingView_RevisionClouds.md) | Returns the collection of revision clouds on this drawing view. |
| [Rotation](../DrawingView/DrawingView_Rotation.md) | Read-write property that gets and sets the absolute rotation angle of the drawing view in radians. The value can either be positive (counter-clockwise rotation) or negative (clockwise rotation). |
| [Scale](../DrawingView/DrawingView_Scale.md) | Gets or sets the Model-to-PaperSpace scale of this particular Drawing View. |
| [ScaleFromBase](../DrawingView/DrawingView_ScaleFromBase.md) | Gets and sets whether the scale of the view derives from the parent view or not. |
| [ScaleString](../DrawingView/DrawingView_ScaleString.md) | Gets or sets the Model-to-PaperSpace scale in string format of this particular Drawing View. |
| [SheetToDrawingViewTransform](../DrawingView/DrawingView_SheetToDrawingViewTransform.md) | Property that returns the transformation from sheet space to the drawing view coordinate space. |
| [SheetToModelTransform](../DrawingView/DrawingView_SheetToModelTransform.md) | Property that returns the transformation from sheet coordinate space to the model space. |
| [ShowLabel](../DrawingView/DrawingView_ShowLabel.md) | Gets and sets whether to show the label of the drawing view on the sheet. |
| [ShowTrails](../DrawingView/DrawingView_ShowTrails.md) | Gets and set whether to show the trails or not for a drawing view of a presentation. |
| [Sketches](../DrawingView/DrawingView_Sketches.md) | Property that returns the DrawingSketches collection object for the sheet. This object provides access to all of the sketches that have been created on the sheet and provides functionality to create new sketches. |
| [StandardPartsSectionBehavior](../DrawingView/DrawingView_StandardPartsSectionBehavior.md) | Gets and sets the sectioning behavior for standard parts in drawing views of assemblies. |
| [Suppressed](../DrawingView/DrawingView_Suppressed.md) | Gets and sets whether this drawing view is suppressed or not. |
| [Top](../DrawingView/DrawingView_Top.md) | Property that specifies the position of the top edge of the drawing view. |
| [Type](../DrawingView/DrawingView_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../DrawingView/DrawingView_UpToDate.md) | Property that returns whether the drawing view is up to date with respect to the model. |
| [ViewAnnotation](../DrawingView/DrawingView_ViewAnnotation.md) | Read-only property that returns the drawing view annotation object. |
| [ViewJustification](../DrawingView/DrawingView_ViewJustification.md) | Gets and sets the view justification. |
| [ViewOrientationFromBase](../DrawingView/DrawingView_ViewOrientationFromBase.md) | Gets and sets whether the view should inherit the orientation from the base view. |
| [ViewStyle](../DrawingView/DrawingView_ViewStyle.md) | Gets and sets the drawing view style. |
| [ViewType](../DrawingView/DrawingView_ViewType.md) | Property returning an DrawingViewTypeEnum constant indicating the type of view. |
| [Width](../DrawingView/DrawingView_Width.md) | Property that specifies the width of the drawing view. The view width cannot be set but is defined by the contents of the view. |

## Accessed From

[Balloon.ParentView](../Balloon/Balloon_ParentView.md), [BreakOperation.Parent](../BreakOperation/BreakOperation_Parent.md), [BreakOutOperation.Parent](../BreakOutOperation/BreakOutOperation_Parent.md), [CropOperation.Parent](../CropOperation/CropOperation_Parent.md), [DetailDrawingView.CopyTo](../DetailDrawingView/DetailDrawingView_CopyTo.md), [DetailDrawingView.MoveTo](../DetailDrawingView/DetailDrawingView_MoveTo.md), [DetailDrawingView.ParentView](../DetailDrawingView/DetailDrawingView_ParentView.md), [DrawingCurve.Parent](../DrawingCurve/DrawingCurve_Parent.md), [DrawingDocument.ProcessViewSelection](../DrawingDocument/DrawingDocument_ProcessViewSelection.md), [DrawingView.CopyTo](../DrawingView/DrawingView_CopyTo.md), [DrawingView.MoveTo](../DrawingView/DrawingView_MoveTo.md), [DrawingView.ParentView](../DrawingView/DrawingView_ParentView.md), [DrawingViewAnnotation.Parent](../DrawingViewAnnotation/DrawingViewAnnotation_Parent.md), [DrawingViewEvents.Parent](../DrawingViewEvents/DrawingViewEvents_Parent.md), [DrawingViewHatchRegion.Parent](../DrawingViewHatchRegion/DrawingViewHatchRegion_Parent.md), [DrawingViewLabel.Parent](../DrawingViewLabel/DrawingViewLabel_Parent.md), [DrawingViews.AddAssociativeDraftView](../DrawingViews/DrawingViews_AddAssociativeDraftView.md), [DrawingViews.AddAuxiliaryView](../DrawingViews/DrawingViews_AddAuxiliaryView.md), [DrawingViews.AddBaseView](../DrawingViews/DrawingViews_AddBaseView.md), [DrawingViews.AddDraftView](../DrawingViews/DrawingViews_AddDraftView.md), [DrawingViews.AddOverlayView](../DrawingViews/DrawingViews_AddOverlayView.md), [DrawingViews.AddOverlayView2](../DrawingViews/DrawingViews_AddOverlayView2.md), [DrawingViews.AddProjectedView](../DrawingViews/DrawingViews_AddProjectedView.md), [DrawingViews.Item](../DrawingViews/DrawingViews_Item.md), [HoleTable.ParentView](../HoleTable/HoleTable_ParentView.md), [SectionDrawingView.CopyTo](../SectionDrawingView/SectionDrawingView_CopyTo.md), [SectionDrawingView.MoveTo](../SectionDrawingView/SectionDrawingView_MoveTo.md), [SectionDrawingView.ParentView](../SectionDrawingView/SectionDrawingView_ParentView.md)

## Derived Classes

[DetailDrawingView](../DetailDrawingView/DetailDrawingView.md), [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Baseline dimension sets](../../sample-programs/BaselineDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a baseline set dimension in a drawing. |
| [Creation of a break operation in a drawing view](../../sample-programs/BreakOperations_Add_Sample.md) | Demonstrates the creation of a break operation. |
| [Chain dimensions sets](../../sample-programs/ChainDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a chain dimension set in a drawing. |
| [Create BreakOpertion by Sketch Sample](../../sample-programs/CreateBreakOpertionBySketchSample_Sample.md) | This sample demonstrates how to create a break operation using a sketch. |
| [CropOperation creation sample](../../sample-programs/CropOperationCreationSample_Sample.md) | This sample demonstrates how to create a crop operation for a drawing view bases on a sketch under the drawing view. |
| [Creating hole tables](../../sample-programs/HoleTables_Add_Sample.md) | This sample demonstrates the creation of hole tables in a drawing. |
| [Move DrawingViewAnnotation Text Position Sample](../../sample-programs/MoveViewAnnotationTextPositionSample_Sample.md) | This sample demonstrates how to move the text position of drawing view annotation. Create a detail or section view before running this sample. |
| [Creating a parts list](../../sample-programs/PartsLists_Add_Sample.md) | This sample demonstrates the creation of a parts list. The parts list is placed at the top right corner of the border if one exists, else it is placed at the top right corner of the sheet. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |