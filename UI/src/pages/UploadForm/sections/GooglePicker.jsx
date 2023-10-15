import React, { useState } from 'react';
import useDrivePicker from 'react-google-drive-picker';
import MKButton from "components/MKButton";

const GooglePicker = ({ receivedData } ) => {
    const [openPicker] = useDrivePicker();

    const handleOpenPicker = () => {
        gapi.load('client:auth2', () => {
            gapi.client
                .init({
                    apiKey: 'AIzaSyBxc5cuRdzvT85F9jonRuJG9bw0y5HyAcg',
                })
                .then(() => {
                    let tokenInfo = gapi.auth.getToken();
                    const pickerConfig: any = {
                        clientId: '962959448381-qeksmmipf0v5qk0hcrrbij1vdle18399.apps.googleusercontent.com',
                        developerKey: 'AIzaSyBxc5cuRdzvT85F9jonRuJG9bw0y5HyAcg',
                        viewId: 'DOCS',
                        viewMimeTypes: 'image/jpeg,image/png,image/gif',
                        token: tokenInfo ? tokenInfo.access_token : null,
                        showUploadView: true,
                        showUploadFolders: true,
                        supportDrives: true,
                        multiselect: true,
                        callbackFunction: (data) => {
                            console.log(data);
                            receivedData(data);
                            
                  
                        },
                    };
                    openPicker(pickerConfig);
                });
        });
    };

    return (
        <MKButton variant="gradient" color="info" onClick={() => handleOpenPicker()}>
            Upload Images and Submit
        </MKButton>
    );
};

export default GooglePicker;