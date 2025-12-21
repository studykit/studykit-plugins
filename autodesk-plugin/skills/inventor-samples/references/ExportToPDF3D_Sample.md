# Export to 3D PDF

## Description

The 3D PDF converter is to translate Inventor model to 3D PDF format, but not like the other translators this function is implemented in an ApplicationAddin, so it is a bit different to be used via API. Below sample demonstrates how to use the ApplicationAddin.Automation to get the function to export Inventor model to 3D PDF.

## Code Samples

* [VBA](#VBA)
* [C#](#C#)
* [C++](#C++)

Open a part document, and new a design view named "View1", and run below VBA code:

|  |
| --- |
| Copy Code |

```
Public Sub PublishTo3DPDF()
    ' Get the 3D PDF Add-In.
    Dim oPDFAddIn As ApplicationAddIn
    Dim oAddin As ApplicationAddIn
    For Each oAddin In ThisApplication.ApplicationAddIns
        If oAddin.ClassIdString = "{3EE52B28-D6E0-4EA4-8AA6-C2A266DEBB88}" Then
            Set oPDFAddIn = oAddin
            Exit For
        End If
    Next

    If oPDFAddIn Is Nothing Then
        MsgBox "Inventor 3D PDF Addin not loaded."
        Exit Sub
    End If

    Dim oPDFConvertor3D
    Set oPDFConvertor3D = oPDFAddIn.Automation

    'Set a reference to the active document (the document to be published).
    Dim oDocument As Document
    Set oDocument = ThisApplication.ActiveDocument

    ' Create a NameValueMap object as Options
    Dim oOptions As NameValueMap
    Set oOptions = ThisApplication.TransientObjects.CreateNameValueMap

    ' Options
    oOptions.Value("FileOutputLocation") = "c:\temp\test.pdf"
    oOptions.Value("ExportAnnotations") = 1
    oOptions.Value("ExportWokFeatures") = 1
    oOptions.Value("GenerateAndAttachSTEPFile") = True
    oOptions.Value("VisualizationQuality") = kHigh

    ' Set the properties to export
    Dim sProps(0) As String
    sProps(0) = "{F29F85E0-4FF9-1068-AB91-08002B27B3D9}:Title"  ' Title

    oOptions.Value("ExportAllProperties") = False
    oOptions.Value("ExportProperties") = sProps

    ' Set the design views to export
    Dim sDesignViews(1) As String
    sDesignViews(0) = "Master"
    sDesignViews(1) = "View1"

    oOptions.Value("ExportDesignViewRepresentations") = sDesignViews

    'Publish document.
    Call oPDFConvertor3D.Publish(oDocument, oOptions)
End Sub
```

Open a part document, and new a design view named "View1", and copy below C# code to a project to run it.

|  |
| --- |
| Copy Code |

```
public void Export3DPdf()
        {
            Inventor.Application InvApp = mApp;

            Inventor.ApplicationAddIn  PDFAddin = null ;

            foreach (ApplicationAddIn appAddin in mApp.ApplicationAddIns )
            {
                if (appAddin.ClassIdString == "{3EE52B28-D6E0-4EA4-8AA6-C2A266DEBB88}")
                {
                    PDFAddin =  appAddin;
                    break;
                }
            }

            dynamic pdfConvertor3d = PDFAddin.Automation;

            Document oDoc = mApp.ActiveDocument;
            // Create a NameValueMap object
            Inventor.NameValueMap oOptions = InvApp.TransientObjects.CreateNameValueMap();

            oOptions.Value["FileOutputLocation"] = @"c:\temp\3DPDF.pdf";
            oOptions.Value["ExportAllProperties"] = true;
            oOptions.Value["GenerateAndAttachSTEPFile"] = true ;
            oOptions.Value["ExportTemplate"] = @"C:\Users\Public\Documents\Autodesk\Inventor 2019\Templates\Sample Part Template.pdf";
            oOptions.Value["VisualizationQuality"] = AccuracyEnum.kHigh;

            //string[] sProps = new string[1];
            //sProps[0] = "{F29F85E0-4FF9-1068-AB91-08002B27B3D9}:Title";
            //oOptions.Value["ExportAllProperties"] = false;
            //oOptions.Value["ExportProperties"] = sProps;

            String[] sDesignViews = new string[] { "Master", "View1" };
            oOptions.Value["ExportDesignViewRepresentations"] = sDesignViews;

            pdfConvertor3d.Publish(oDoc, oOptions);

        }
```

Copy the C++ code to your project, and change the hardcoded file names for the sFileName in ExportToPDF3D to set the document path in your machine, and update the sTemplatePath to specify a proper template according to the doucment type. Then call the ExportToPDF3D to export the document to 3D PDF.

|  |
| --- |
| Copy Code |

```
static HRESULT ExportToPDF3D();
DesignViewRepresentationsPtr GetDesignViewRepresentations(Document* pDocument);
HRESULT GetDesignViews(DesignViewRepresentationsPtr pDVRepresentations, CComSafeArray<BSTR>& sDVs);
HRESULT CreateStepFileOption(NameValueMap *pOptionsStep);

static HRESULT ExportToPDF3D()
{
	HRESULT hr = NOERROR;

	TCHAR Str[_MAX_PATH];

	CLSID InvAppClsid;
	hr = CLSIDFromProgID (L"Inventor.Application", &InvAppClsid);
	if (FAILED(hr)) return hr;

	// Either create a new instance of the application or latch on to the currently active one.
	_tprintf_s (_T("Would you like to create a new Inventor application? (y/n) _: "));
	_tscanf_s (_T("%ls"), Str, _MAX_PATH);

	CComPtr<IUnknown> pInvAppUnk;
	if (toupper (Str[0]) == _T('Y'))
	{
		hr = CoCreateInstance (InvAppClsid, NULL, CLSCTX_LOCAL_SERVER, __uuidof(IUnknown), (void **) &pInvAppUnk);
		if (FAILED (hr))
			_tprintf_s (_T("*** Failed to create a new Inventor application ***\n"));
	}
	else
	{
		hr = ::GetActiveObject (InvAppClsid, NULL, &pInvAppUnk);
		if (FAILED (hr))
			_tprintf_s (_T("*** Could not get hold of an active Inventor application ***\n"));
	}
	if (FAILED(hr)) return hr;

	CComPtr<Application> m_pApplication;//m_pApplication;
	hr = pInvAppUnk->QueryInterface (__uuidof(Application), (void **) &m_pApplication);
	if (FAILED(hr)) return hr;

	hr = m_pApplication->put_Visible(-1);
	if (FAILED(hr)) return hr;

	TransientObjectsPtr pTransObj;
	hr = m_pApplication->get_TransientObjects(&pTransObj);
	if (FAILED(hr))		return hr;

	CComBSTR sFileName = "C:\\Temp\\Assembly1.iam";

	CComPtr<Documents> pDocs;
	hr = m_pApplication->get_Documents(&pDocs);
	if (FAILED(hr)) return hr;

	DocumentPtr pDoc = nullptr;
	hr = pDocs->Open(sFileName, VARIANT_TRUE, &pDoc);
	if (FAILED(hr)) return hr;

	//get NameValueMap
	CComPtr<NameValueMap> pOptionsPDF = nullptr;
	hr = pTransObj->CreateNameValueMap(&pOptionsPDF);
	if (FAILED(hr))			return hr;

	// Set the option "FileOutputLocation" to NameValueMap
	CComBSTR sOutputFilePath = "C:\\Users\\Temp\\Assembly1.pdf";
	hr = pOptionsPDF->MethodAdd(_T("FileOutputLocation"), CComVariant(sOutputFilePath));
	if (FAILED(hr))			return hr;

	// Set the option "ExportTemplate" to NameValueMap
	CComBSTR sTemplatePath = "C:\\Users\\Public\\Documents\\Autodesk\\Inventor 2019\\Templates\\Sample Assembly Template.pdf";
	hr = pOptionsPDF->MethodAdd(_T("ExportTemplate"), CComVariant(sTemplatePath));
	if (FAILED(hr))		return hr;

	// Set the option "VisualizationQuality" to NameValueMap
	AccuracyEnum eVisualizationQuality = kHigh; // kLow  kMedium

	hr = pOptionsPDF->MethodAdd(_T("VisualizationQuality"), CComVariant(eVisualizationQuality));
	if (FAILED(hr))		return hr;

	// Set the option "LimitToEntitiesInDVRs" to NameValueMap
	bool  m_bPublishAllEntities = false;
	hr = pOptionsPDF->MethodAdd(_T("LimitToEntitiesInDVRs"), CComVariant(m_bPublishAllEntities));
	if (FAILED(hr))		return hr;

	// Set the option "ExportAllProperties" to NameValueMap
	bool bExportAllProperties = true;
	hr = pOptionsPDF->MethodAdd(_T("ExportAllProperties"), CComVariant(bExportAllProperties));
	if (FAILED(hr))		return hr;

	if (!bExportAllProperties)
	{
		// Set the option "ExportProperties" to NameValueMap
		CComSafeArray<BSTR> saProperties;
		saProperties.Add(CComBSTR("{F29F85E0-4FF9-1068-AB91-08002B27B3D9}:Title"));
		saProperties.Add(CComBSTR("{D5CDD502-2E9C-101B-9397-08002B2CF9AE}:Company"));
		saProperties.Add(CComBSTR("{32853F0F-3444-11D1-9E93-0060B03C1CA6}:Part Number"));

		hr = pOptionsPDF->MethodAdd(_T("ExportProperties"), CComVariant(saProperties));
		if (FAILED(hr))			return hr;
	}

	// Set the option "ExportDesignViewRepresentations" to NameValueMap
	DesignViewRepresentationsPtr spDVReps = GetDesignViewRepresentations(pDoc);
	CComSafeArray<BSTR> sDesignViews;

	hr = GetDesignViews(spDVReps, sDesignViews);
	if (FAILED(hr))		return hr;

	if (sDesignViews != nullptr)
	{
		hr = pOptionsPDF->MethodAdd(_T("ExportDesignViewRepresentations"), CComVariant(sDesignViews));
		if (FAILED(hr))			return hr;
	}

	// Set the option "GenerateAndAttachSTEPFile" to NameValueMap
	bool bAttachSTEPFile = true;
	hr = pOptionsPDF->MethodAdd(_T("GenerateAndAttachSTEPFile"), CComVariant(bAttachSTEPFile));
	if (FAILED(hr))		return hr;

	if (bAttachSTEPFile)
	{
		//get NameValueMap
		CComPtr<NameValueMap> pOptionsStep = nullptr;
		hr = pTransObj->CreateNameValueMap(&pOptionsStep);
		if (FAILED(hr))			return hr;

		hr = CreateStepFileOption(pOptionsStep);
		if (FAILED(hr))			return hr;

		// Set the option "STEPFileOptions" to NameValueMap
		hr = pOptionsPDF->MethodAdd(_T("STEPFileOptions"), CComVariant(pOptionsStep));
		if (FAILED(hr))			return hr;
	}

	// Set the option "AttachedFiles" to NameValueMap
	CComSafeArray<BSTR> aAttachFiles;
	hr = aAttachFiles.Add(CComBSTR("C:\\temp\\log.pdf"));
	if (FAILED(hr))			return hr;

	hr = pOptionsPDF->MethodAdd(_T("AttachedFiles"), CComVariant(aAttachFiles));
	if (FAILED(hr))			return hr;

	CComPtr<ApplicationAddIns> pInvAppAddIns = nullptr;
	hr = m_pApplication->get_ApplicationAddIns(&pInvAppAddIns);
	if (FAILED(hr))		return hr;

	// Client id of 3D PDf addin
	CComBSTR clsidAddin = CComBSTR(_T("{3EE52B28-D6E0-4EA4-8AA6-C2A266DEBB88}"));

	CComPtr<ApplicationAddIn> pAddin = nullptr;
	hr = pInvAppAddIns->get_ItemById(clsidAddin, &pAddin);

	if (pAddin)
	{
		CComPtr<IDispatch> pAddinAutomaton;
		pAddin->get_Automation(&pAddinAutomaton);

		if (pAddinAutomaton)
		{
			DISPID dispId;
			OLECHAR* name(OLESTR("Publish"));
			hr = pAddinAutomaton->GetIDsOfNames(IID_NULL, &name, 1, LOCALE_SYSTEM_DEFAULT, &dispId);

			if (SUCCEEDED(hr))
			{
				CComVariant varArgs[2];
				varArgs[1] = pDoc.GetInterfacePtr();
				varArgs[0] = pOptionsPDF;
				DISPPARAMS params = { &varArgs[0], NULL, 2, 0 };
				CComVariant vRes;

				hr = pAddinAutomaton->Invoke(dispId, IID_NULL, LOCALE_SYSTEM_DEFAULT, DISPATCH_METHOD, &params, &vRes, NULL, NULL);
			}
		}
	}

	return hr;
}

DesignViewRepresentationsPtr GetDesignViewRepresentations(Document* pDocument)
{
	if (pDocument == nullptr)
		return nullptr;

	HRESULT hr = S_OK;
	RepresentationsManagerPtr pRepsMgr;

	AssemblyDocumentPtr spAsmDoc = pDocument;
	if (spAsmDoc != nullptr)
	{
		AssemblyComponentDefinitionPtr pAsmDef;
		hr = spAsmDoc->get_ComponentDefinition(&pAsmDef);
		if (FAILED(hr))
			return nullptr;

		hr = pAsmDef->get_RepresentationsManager(&pRepsMgr);
		if (FAILED(hr))
			return nullptr;
	}
	else
	{
		PartDocumentPtr pPartDoc = pDocument;
		if (pPartDoc != nullptr)
		{
			PartComponentDefinitionPtr pPartDef;
			hr = pPartDoc->get_ComponentDefinition(&pPartDef);
			if (FAILED(hr))
				return nullptr;

			hr = pPartDef->get_RepresentationsManager(&pRepsMgr);
			if (FAILED(hr))
				return nullptr;
		}
	}

	if (pRepsMgr != nullptr)
	{
		DesignViewRepresentationsPtr pDVRepresentations;
		hr = pRepsMgr->get_DesignViewRepresentations(&pDVRepresentations);
		if (FAILED(hr))
			return nullptr;

		return pDVRepresentations;
	}

	return nullptr;
}

HRESULT GetDesignViews(DesignViewRepresentationsPtr pDVRepresentations, CComSafeArray<BSTR>& sDVs)
{
	HRESULT hr = S_OK;

	long lCountDV = 0;
	hr = pDVRepresentations->get_Count(&lCountDV);
	if (FAILED(hr))
		return hr;

	for (int i = 0; i < lCountDV; i++)
	{
		DesignViewRepresentationPtr pDV = nullptr;
		CComVariant varIndex(i + 1);
		hr = pDVRepresentations->get_Item(varIndex, &pDV);
		if (FAILED(hr))
			continue;

		DesignViewTypeEnum viewType;
		pDV->get_DesignViewType(&viewType);
		if (viewType == kTransientDesignViewType)
			continue;

		if (VARIANT_TRUE) {
			VARIANT_BOOL bPublishDV;
			hr = pDV->get_Publish(&bPublishDV);

			if (FAILED(hr) || bPublishDV == VARIANT_FALSE)
				continue;
		}

		CComBSTR bstrNameDV;
		pDV->get_Name(&bstrNameDV);
		sDVs.Add(CComBSTR(bstrNameDV));
	}

	return S_OK;
}

HRESULT CreateStepFileOption(NameValueMap *pOptionsStep)
{
	HRESULT hr = S_OK;

	// check input map pointer
	if (pOptionsStep == nullptr)
		return S_FALSE;

	// Set the option "ApplicationProtocolType" to NameValueMap
	// Valid values: eAP203 = 2, eAP214IS = 4 and eAP242 = 5
	int iApplicationProtocolType = 5;
	hr = pOptionsStep->MethodAdd(_T("ApplicationProtocolType"), CComVariant(iApplicationProtocolType));
	if (FAILED(hr))		return hr;

	// Set the option "Author" to NameValueMap
	CComBSTR sAuthor = "";
	hr = pOptionsStep->MethodAdd(_T("Author"), CComVariant(sAuthor));
	if (FAILED(hr))		return hr;

	// Set the option "Authorization" to NameValueMap
	CComBSTR sAuthorization = "";
	hr = pOptionsStep->MethodAdd(_T("Authorization"), CComVariant(sAuthorization));
	if (FAILED(hr))		return hr;

	// Set the option "Description" to NameValueMap
	CComBSTR sDescription = "";
	hr = pOptionsStep->MethodAdd(_T("Description"), CComVariant(sDescription));
	if (FAILED(hr))
		return hr;

	// Set the option "ExportFitTolerance" to NameValueMap
	double dTolerance = 0.001;
	hr = pOptionsStep->MethodAdd(_T("ExportFitTolerance"), CComVariant(dTolerance));
	if (FAILED(hr))		return hr;

	// Set the option "Organization" to NameValueMap
	CComBSTR sOrganization = "";
	hr = pOptionsStep->MethodAdd(_T("Organization"), CComVariant(sOrganization));
	if (FAILED(hr))		return hr;

	// Set the option "IncludeSketches" to NameValueMap
	bool bExportSketches = true;
	hr = pOptionsStep->MethodAdd(_T("IncludeSketches"), CComVariant(bExportSketches));
	if (FAILED(hr))		return hr;

	return hr;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |