_y='e.g. CTRL + SHIFT'
_x='In range 80 - 1000 ms'
_w='Fire rate'
_v='Cancel'
_u='delete'
_t='keyboard'
_s='win32api'
_r='VALORANT  '
_q='#3f77e0'
_p='#ba3a3a'
_o='#42bd6b'
_n='-topmost'
_m='burst'
_l='sniper'
_k='custom mode'
_j='add'
_i='mouse0'
_h='mouse2'
_g='off'
_f='right'
_e='mouse1'
_d='sheriff'
_c='guardian'
_b='fast'
_a='mute'
_Z='top'
_Y='capslock+Alt'
_X='ctrl+p'
_W='hold_to_toggle'
_V='height'
_U='width'
_T='vandal'
_S='menu_key'
_R='on_off_hotkey'
_Q='shoot_when_moving_hotkey'
_P='left'
_O=None
_N='update'
_M='x'
_L='name'
_K='hold_key'
_J='modes'
_I='TkDefaultFont'
_H='null'
_G='hotkey'
_F='fire_rate'
_E=False
_D='preferences'
_C=True
_B='bold'
_A='w'
import importlib
from subprocess import call
import subprocess,time,sys,os
required_packages=['mss','PIL','time','colorsys','sys','tkinter','winsound','requests','threading','os','ctypes','random','customtkinter',_s,_t]
def install(package):subprocess.check_call([sys.executable,'-m','pip','install',package])
def check_and_install_packages(packages):
        B=_C
        for A in packages:
                try:__import__(A)
                except ImportError:
                        print(f"{A} is not installed. Installing now...")
                        if A=='PIL':A='Pillow'
                        if A==_s:A='pypiwin32'
                        install(A);B=_E
        return B
if check_and_install_packages([A.split('==')[0]for A in required_packages]):print('All required packages are installed!');os.system('cls');print('Script is running...')
else:print('Restarting the script to apply changes...');os.execv(sys.executable,[sys.executable]+sys.argv)
import ctypes,sys,os,mss
from PIL import Image
import time,colorsys,sys
try:__import__(_t)
except ImportError:time.sleep(10)
import keyboard,tkinter as tk,winsound,requests,threading,PIL.ImageGrab,PIL.Image,os,ctypes,random,signal,win32api,win32con,time,json,socket,json,requests,customtkinter,tkinter,tempfile,win32gui,win32con,time
class ActiveValues:user_key='';user_uuid='';user_type='';colorSelected=1;last_frame_moving=_E;moving=_E;shoot_when_moving=_E;latency=220;hold=0;toggle=_C;strafeToggle=_C;grabzone=4;modes=[];sniper_mode=_E;burst_mode=_E;monitors=[];selectedMonitorIndex=-1;VK_L=76;KEYEVENTF_EXTENDEDKEY=1;KEYEVENTF_KEYUP=2;mss='lexiPteG';formatted=[];connected=_E;scan=_E
class Config:
        '\n    Holds configuration settings for the application.\n    '
        def __init__(A,active_values):A.active_values=active_values;A.CONFIG_FILE=os.path.join(os.path.expanduser('~'),'config.json');A.config={_D:{_K:'v',_S:'t',_W:0,_a:0,_Q:_X,_R:_Y},_J:{_b:{_L:_b,_F:80,_G:_H},_T:{_L:_T,_F:180,_G:_H},_c:{_L:_c,_F:300,_G:_H},_d:{_L:_d,_F:500,_G:_H}}};A.load_config()
        def open_config_with_notepad(B):
                '\n        Opens the specified config file with Windows Notepad in non-blocking mode.\n        ';A=B.CONFIG_FILE
                if os.path.exists(A):
                        try:subprocess.Popen(['notepad.exe',A])
                        except FileNotFoundError:print('Error: Notepad is not available on this system.')
                        except Exception as C:print(f"An error occurred: {C}")
                else:print(f"Config file not found at: {A}")
        def edit_config(G,key_path,new_value=_O,action=_N):
                "\n        Updates, deletes, or adds a nested dictionary entry given a path to the key.\n\n        Args:\n            data (dict): The dictionary to update.\n            key_path (str): The path to the key in the format '[key1][key2][key3]'.\n            new_value: The new value to set for the specified key (used only for update).\n            action (str): The action to perform, either 'update', 'delete', or 'add'.\n\n        Returns:\n            dict: The updated dictionary.\n        ";'\n        validation \n        ';I='[preferences][hold_key]';E=action;B=key_path;A=new_value
                if E==_N:
                        J=[_K,_S,_Q,_R,_G]
                        if any(A in B for A in J):
                                if B==I and(A==_e or A==_h or A==_i):0
                                elif'[hotkey]'in B:
                                        try:keyboard.is_pressed(A)
                                        except Exception as K:print(K);print('Invalid hotkey. Please enter a valid hotkey.');A=_H
                                else:
                                        try:keyboard.is_pressed(A)
                                        except:
                                                if B=='[preferences][menu_key]':A='T';print('Invalid Menu Hotkey , using <T> instead')
                                                elif B=='[preferences][shoot_when_moving_hotkey]':A=_X;print('Invalid Menu Hotkey , using <ctrl+p> instead')
                                                elif B=='[preferences][on_off_hotkey]':A=_Y;print('Invalid Menu Hotkey , using <capslock+Alt> instead')
                                                elif B==I:A='v';print('Invalid Hold Key, using <v> instead')
                        elif _F in B:
                                try:int(A)
                                except:print('Invalid fire rate. Please enter a valid integer.')
                                if int(A)<80:print('Fire rate must be greater than 80');A='80'
                                elif int(A)>1000:print('Fire rate must be less than 1000');A='1000'
                                A=int(A)
                H=B.strip('[]').split('][');C=G.config
                for F in H[:-1]:
                        if F not in C:
                                if E==_j:C[F]={}
                                else:raise KeyError(f"Key '{F}' not found in the dictionary.")
                        C=C[F]
                D=H[-1]
                if E==_N:C[D]=A
                elif E==_u:
                        if D not in C:raise KeyError(f"Key '{D}' not found in the dictionary.")
                        del C[D]
                elif E==_j:
                        if D in C:raise KeyError(f"Key '{D}' already exists. Use 'update' to modify it.")
                        C[D]=A
                else:raise ValueError("Invalid action. Use 'update', 'delete', or 'add'.")
                G.save_config();G.store_mode_names_in_list();gui.update_modes_dropdown()
        def validate_config(L,data):
                '\n        Validates the given configuration dictionary.\n\n        Args:\n            config (dict): The configuration dictionary to validate.\n\n        Returns:\n            dict: The validated configuration dictionary.\n        ';C=data;A=C.get(_D,{});D=A.get(_K,'')
                if D not in[_e,_h,_i]:
                        try:keyboard.is_pressed(D)
                        except:D='v';print("Invalid hold_key. Using default value 'v'.")
                A[_K]=D;G=A.get(_S,'')
                try:keyboard.is_pressed(G)
                except:G='T';print("Invalid menu_key. Using default value 'T'.")
                A[_S]=G;H=A.get(_Q,'')
                try:keyboard.is_pressed(H)
                except:H=_X;print("Invalid shoot_when_moving_hotkey. Using default value 'ctrl+p'.")
                A[_Q]=H;I=A.get(_R,'')
                try:keyboard.is_pressed(I)
                except:I=_Y;print("Invalid on_off_hotkey. Using default value 'capslock+Alt'.")
                A[_R]=I;C[_D]=A;J=C.get(_J,{})
                for(K,E)in J.items():
                        B=E.get(_F,0)
                        if not isinstance(B,int)or B<80 or B>1000:B=max(80,min(B,1000))if isinstance(B,int)else 80;print(f"Invalid fire_rate for mode '{K}'. Using adjusted value '{B}'.")
                        E[_F]=B;F=E.get(_G,'')
                        if F not in['',_H]:
                                try:keyboard.is_pressed(F)
                                except:F=_H;print(f"Invalid hotkey for mode '{K}'. Using default value 'null'.")
                        E[_G]=F
                C[_J]=J;return C
        def load_config(A):
                C={}
                if not A.active_values.user_type==_k:A.store_mode_names_in_list();return
                else:print('loading custom config')
                try:
                        with open(A.CONFIG_FILE,'r')as B:C=json.load(B);A.config=A.validate_config(C);A.save_config();A.store_mode_names_in_list();return
                except Exception as E:
                        print(E);print('Config file not found. Loading default configuration.');D={_D:{_K:'v',_S:'t',_W:0,_a:0,_Q:_X,_R:_Y},_J:{_b:{_L:_b,_F:80,_G:_H},_T:{_L:_T,_F:180,_G:_H},_c:{_L:_c,_F:300,_G:_H},_d:{_L:_d,_F:500,_G:_H},_l:{_L:_l,_F:90,_G:_H},_m:{_L:_m,_F:250,_G:_H}}}
                        with open(A.CONFIG_FILE,_A)as B:json.dump(D,B,indent=4)
                        A.config=D;A.store_mode_names_in_list();return
        def save_config(A):
                with open(A.CONFIG_FILE,_A)as B:json.dump(A.config,B,indent=4)
        def store_mode_names_in_list(A):
                active_values.modes=[]
                for(C,B)in A.config[_J].items():active_values.modes.append(B[_L])
import win32security
class Auth:
        URL='https://thunderous-froyo-4147d2.netlify.app/.netlify/functions/TurboApi'
        def __init__(A):A.user_key=input('Enter the key:');A.user_uuid=A.get_system_uuid();A.type=_O;A.termination_thread=_O;A.active_values=active_values;A.get_api_response()
        def get_system_uuid(E):
                try:A=win32api.GetUserName();B,F,type=win32security.LookupAccountName(_O,A);C=win32security.ConvertSidToStringSid(B);return C
                except Exception as D:print(f"Error: {D}");return
        def get_api_response(A):
                A.active_values.user_uuid=A.user_uuid;A.active_values.user_key=A.user_key;B=requests.get(A.URL,params={'key':A.user_key,'UUID':A.user_uuid})
                if B.status_code==200:
                        C=B.json()
                        if C.get('valid'):A.process_response(C);os.system('cls')
                        else:A.exit_with_error(B)
                else:A.exit_with_error(B)
        def process_response(A,data):
                B={'0':'test mode','1':'trial mode','2':'standard mode','3':_k};A.type=data.get('type');active_values.user_type=B.get(A.type)
                if A.type=='0'and A.termination_thread is _O:A.start_termination_thread()
        def exit_with_error(A,response):print('There was a problem...');print(f"Error: {response.json().get("message")} , contact support");time.sleep(49);os._exit(1)
        def start_termination_thread(A):A.termination_thread=threading.Thread(target=A.termination_loop);A.termination_thread.start()
        def termination_loop(D):
                print('\n');print('!!The script is running in LIMITED TEST mode!!');print('It will close itself after 2 hours');A=7200
                while A>0:
                        A-=1;B=A/60;C=round(B,2)
                        if A%60==0:print(f"Time left: {C} minutes")
                        time.sleep(1)
                print("Time's up! Exiting...");os._exit(0)
import ctypes
from ctypes import windll
import colorsys,ctypes
from ctypes import windll
import time
from concurrent.futures import ThreadPoolExecutor,as_completed
class Camera:
        def __init__(A):A.active_values=active_values;A.monitors=[];A.formatted_monitors=[];A.active_values=active_values;A.format_monitors();A.set_center_from_selected_monitor();A.PURPLE_H_UPPER,A.PURPLE_S_UPPER,A.PURPLE_V_UPPER=330,100,101;A.PURPLE_H_LOWER,A.PURPLE_S_LOWER,A.PURPLE_V_LOWER=240,35,65;A.YELLOW_H_UPPER,A.YELLOW_S_UPPER,A.YELLOW_V_UPPER=70,90,100;A.YELLOW_H_LOWER,A.YELLOW_S_LOWER,A.YELLOW_V_LOWER=50,45,60;A.RED_H_UPPER,A.RED_S_UPPER,A.RED_V_UPPER,A.RED_H_UPPER2=0,100,100,14;A.RED_H_LOWER,A.RED_S_LOWER,A.RED_V_LOWER=341,35,54;A.WHITE_S_UPPER,A.WHITE_V_UPPER=10,100;A.WHITE_S_LOWER,A.WHITE_V_LOWER=0,90;B=ctypes.windll.user32;A.center_x=B.GetSystemMetrics(0)//2;A.center_y=B.GetSystemMetrics(1)//2;A.hdc=windll.user32.GetDC(0)
        def set_center_from_selected_monitor(A):
                C=abs(A.active_values.selectedMonitorIndex)-1
                if 0<=C<len(A.monitors):B=A.monitors[C];A.center_x=B[_P]+B[_U]//2;A.center_y=B[_Z]+B[_V]//2;print(f"[Camera] Scan center set to monitor {C+1} at ({A.center_x}, {A.center_y})")
        def format_monitors(B):
                with mss.mss()as F:
                        B.monitors=[]
                        for A in F.monitors[1:]:
                                if _P in A and _Z in A and _U in A and _V in A:B.monitors.append(A)
                        B.monitors.reverse()
                B.formatted_monitors=[]
                for(C,A)in enumerate(B.monitors,start=1):
                        if _P in A and _Z in A and _U in A and _V in A:G=f"{A[_V]} x {A[_U]}";B.formatted_monitors.append(f"{C} : {G}")
                for C in range(len(B.formatted_monitors)):D=B.formatted_monitors[C].split(' : ');H=D[0].strip();E=D[1].split(' x ');I=E[0].strip();J=E[1].strip();B.formatted_monitors[C]=f" -{H}-\n{J}\n{I}";B.active_values.formatted=B.formatted_monitors
        def check_for_white(A,r,g,b):return all([r>=251,g>=251,b>=251])
        def approx(A,r,g,b,color):
                C=color;r,g,b=[A/255. for A in(r,g,b)];F,G,H=colorsys.rgb_to_hsv(r,g,b);B=round(F*360);D=round(G*100);E=round(H*100)
                if C==0:return all([A.YELLOW_H_LOWER<=B<=A.YELLOW_H_UPPER,A.YELLOW_S_LOWER<=D<=A.YELLOW_S_UPPER,A.YELLOW_V_LOWER<=E<=A.YELLOW_V_UPPER])
                elif C==1:return all([A.PURPLE_H_LOWER<=B<=A.PURPLE_H_UPPER,A.PURPLE_S_LOWER<=D<=A.PURPLE_S_UPPER,A.PURPLE_V_LOWER<=E<=A.PURPLE_V_UPPER])
                elif C==2:return all([A.RED_H_LOWER<=B or B<=A.RED_H_UPPER2,A.RED_S_LOWER<=D<=A.RED_S_UPPER,A.RED_V_LOWER<=E<=A.RED_V_UPPER])
        def _get_pixel(B,x,y):A=windll.gdi32.GetPixel(B.hdc,x,y);C=A&255;D=A>>8&255;E=A>>16&255;return x,y,C,D,E
        def _get_pixel_fast(B,x,y):
                'MSS fast screenshot'
                if active_values.scan:
                        from mss import mss
                        with mss()as G:A=G.monitors[active_values.selectedMonitorIndex];H=int(A[_P]+A[_U]/2-active_values.grabzone),int(A[_Z]+A[_V]/2-active_values.grabzone-15),int(A[_P]+A[_U]/2+active_values.grabzone),int(A[_Z]+A[_V]/2);I=G.grab(H);C,D,E=I.pixel(x,y);return(x,y,C,D,E)if B.approx(C,D,E,B.active_values.colorSelected)else _O
                J=lambda:getattr(ctypes.windll.gdi32,active_values.mss[::-1]);F=J()(B.hdc,x,y);C=F*1&255;D=(F>>8)*1&255;E=(F>>16)*1&255
                if B.approx(C,D,E,B.active_values.colorSelected):return x,y,C,D,E
        def grab_method2(A):
                'Check center first, then scan edges';G=10+active_values.grabzone;D=G//2;B=A._get_pixel_fast(A.center_x,A.center_y)
                if B:return B
                H=A.center_x-D;I=A.center_x+(G-D-1);J=A.center_y-D;K=A.center_y+(G-D-1);C=[]
                for E in range(H,I+1):C.append((E,J));C.append((E,K))
                for F in range(J+1,K):C.append((H,F));C.append((I,F))
                for(E,F)in C:
                        B=A._get_pixel_fast(E,F)
                        if B:return B
        def grab(A):
                'Capture pixels in parallel, stop early if a matching pixel is found.';C=9;B=C//2;D=[(A.center_x+E,A.center_y+D)for D in range(-B,C-B)for E in range(-B,C-B)]
                def H(r,g,b):return A.approx(r,g,b,active_values.colorSelected)
                with ThreadPoolExecutor(max_workers=min(len(D),32))as I:
                        J={I.submit(A._get_pixel,B,C):(B,C)for(B,C)in D}
                        for K in as_completed(J):
                                L,M,E,F,G=K.result()
                                if H(E,F,G):return L,M,E,F,G
        def __del__(A):windll.user32.ReleaseDC(0,A.hdc)
import sys,ctypes,win32gui,win32con,time
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')
class CONFIG_GUI:
        def __init__(A,root,config_class):B=config_class;A.root=root;A.root.title('turbo custom config');A.root.geometry('300x520');A.root.attributes(_n,_C);A.config_class=B;A.config=B.config;A.root.tab_view=customtkinter.CTkTabview(A.root);A.root.tab_view.pack(fill='both',expand=_C,padx=20,pady=20);A.preferences_tab=A.root.tab_view.add('Preferences');A.mode_editor_tab=A.root.tab_view.add('Mode Editor');A.mode_creator_tab=A.root.tab_view.add('Mode Creator');A.setup_preferences_tab();A.setup_mode_editor_tab();A.setup_mode_creator_tab()
        def setup_preferences_tab(A):B=A.config.get(_D,{});customtkinter.CTkLabel(A.preferences_tab,text='ON / OFF hotkey',font=(_I,14,_B)).pack(anchor=_A,pady=5);A.on_off_hotkey_entry=customtkinter.CTkEntry(A.preferences_tab,placeholder_text=_Y);A.on_off_hotkey_entry.insert(0,B.get(_R,''));A.on_off_hotkey_entry.pack(fill=_M,padx=10,pady=5);customtkinter.CTkLabel(A.preferences_tab,text='Shoot while moving hotkey',font=(_I,14,_B)).pack(anchor=_A,pady=5);A.shoot_when_moving_hotkey_entry=customtkinter.CTkEntry(A.preferences_tab,placeholder_text=_X);A.shoot_when_moving_hotkey_entry.insert(0,B.get(_Q,''));A.shoot_when_moving_hotkey_entry.pack(fill=_M,padx=10,pady=5);A.hold_to_toggle_checkbox=customtkinter.CTkCheckBox(A.preferences_tab,text='Hold mode (hold to activate)',variable=customtkinter.BooleanVar(value=B.get(_W,_E)),font=(_I,14,_B));A.hold_to_toggle_checkbox.pack(anchor=_A,padx=10,pady=5);customtkinter.CTkLabel(A.preferences_tab,text='Hold to activate key',font=(_I,14,_B)).pack(anchor=_A,pady=5);A.hold_key_entry=customtkinter.CTkEntry(A.preferences_tab,placeholder_text=_e);A.hold_key_entry.insert(0,B.get(_K,''));A.hold_key_entry.pack(fill=_M,padx=10,pady=5);customtkinter.CTkLabel(A.preferences_tab,text='Menu key',font=(_I,14,_B)).pack(anchor=_A,pady=5);A.menu_key_entry=customtkinter.CTkEntry(A.preferences_tab,placeholder_text='f');A.menu_key_entry.insert(0,B.get(_S,''));A.menu_key_entry.pack(fill=_M,padx=10,pady=5);A.mute_checkbox=customtkinter.CTkCheckBox(A.preferences_tab,text='Mute all sounds (on / off / modes)',variable=customtkinter.BooleanVar(value=B.get(_a,_E)));A.mute_checkbox.pack(anchor=_A,padx=10,pady=5);C=customtkinter.CTkFrame(A.preferences_tab);C.pack(fill=_M,pady=10);customtkinter.CTkButton(C,text='Submit',fg_color=_o,command=A.save_preferences).pack(side=_P,padx=5,expand=_C);customtkinter.CTkButton(C,text=_v,fg_color=_p,command=A.refresh_config_gui_from_config_file).pack(side=_f,padx=5,expand=_C)
        def setup_mode_editor_tab(A):
                for(C,D)in A.config.get(_J,{}).items():B=customtkinter.CTkFrame(A.mode_editor_tab);B.pack(fill=_M,padx=10,pady=5);customtkinter.CTkLabel(B,text=C,font=(_I,14,_B)).pack(side=_P,padx=10);customtkinter.CTkButton(B,text='Edit',fg_color=_q,width=50,command=lambda m=C:A.open_edit_modal(m),font=(_I,14,_B)).pack(side=_f,padx=5);customtkinter.CTkButton(B,text='Delete',fg_color=_p,width=20,command=lambda m=C:A.delete_mode(m),font=(_I,14,_B)).pack(side=_f,padx=5)
        def setup_mode_creator_tab(A):C='consolas';customtkinter.CTkLabel(A.mode_creator_tab,text='Edit config file manually',font=(C,16,_B)).pack(anchor=_A,pady=5);customtkinter.CTkButton(A.mode_creator_tab,text='edit config file',fg_color=_q,command=A.config_class.open_config_with_notepad,font=(_I,14,_B)).pack(anchor=_A,pady=5);customtkinter.CTkButton(A.mode_creator_tab,text='reload config from file ',fg_color=_q,command=A.refresh_config_gui_from_config_file,font=(_I,14,_B)).pack(anchor=_A,pady=5);customtkinter.CTkLabel(A.mode_creator_tab,text='Create a new mode',font=(C,16,_B)).pack(anchor=_A,pady=5);customtkinter.CTkLabel(A.mode_creator_tab,text='Name',font=(_I,14,_B)).pack(anchor=_A,pady=5);A.new_mode_name_entry=customtkinter.CTkEntry(A.mode_creator_tab,placeholder_text='keep it short');A.new_mode_name_entry.pack(fill=_M,padx=10,pady=5);customtkinter.CTkLabel(A.mode_creator_tab,text=_w,font=(_I,14,_B)).pack(anchor=_A,pady=5);A.new_mode_fire_rate_entry=customtkinter.CTkEntry(A.mode_creator_tab,placeholder_text=_x);A.new_mode_fire_rate_entry.pack(fill=_M,padx=10,pady=5);customtkinter.CTkLabel(A.mode_creator_tab,text='Mode hotkey',font=(_I,14,_B)).pack(anchor=_A,pady=5);A.new_mode_hotkey_entry=customtkinter.CTkEntry(A.mode_creator_tab,placeholder_text=_y);A.new_mode_hotkey_entry.pack(fill=_M,padx=10,pady=5);B=customtkinter.CTkFrame(A.mode_creator_tab);B.pack(fill=_M,pady=10);customtkinter.CTkButton(B,text='Add',fg_color=_o,command=A.add_new_mode,font=(_I,14,_B)).pack(side=_P,padx=5,expand=_C)
        def open_edit_modal(B,mode_name):
                C=mode_name;G=B.config[_J].get(C,{});A=customtkinter.CTkToplevel(B.root);A.title('Edit Mode');A.geometry('400x300');A.attributes(_n,_C);customtkinter.CTkLabel(A,text=f"Mode: {C}",font=('Arial',14,_B)).pack(pady=10);customtkinter.CTkLabel(A,text=_w,font=(_I,14,_B)).pack(anchor=_A,pady=5,padx=10);D=customtkinter.CTkEntry(A,placeholder_text=_x);D.insert(0,G.get(_F,''));D.pack(fill=_M,padx=10,pady=5);customtkinter.CTkLabel(A,text='Hotkey',font=(_I,14,_B)).pack(anchor=_A,pady=5,padx=10);E=customtkinter.CTkEntry(A,placeholder_text=_y);E.insert(0,G.get(_G,''));E.pack(fill=_M,padx=10,pady=5)
                def H():F=int(D.get());G=E.get();B.config_class.edit_config(f"[modes][{C}][fire_rate]",F,action=_N);B.config_class.edit_config(f"[modes][{C}][hotkey]",G,action=_N);A.destroy()
                F=customtkinter.CTkFrame(A);F.pack(fill=_M,pady=10);customtkinter.CTkButton(F,text='Save',fg_color=_o,command=H).pack(side=_P,padx=5,expand=_C);customtkinter.CTkButton(F,text=_v,fg_color=_p,command=A.destroy).pack(side=_f,padx=5,expand=_C)
        def delete_mode(A,mode_name):A.config_class.edit_config(f"[modes][{mode_name}]",action=_u);A.refresh_config_gui_from_config_file()
        def add_new_mode(B):
                A=int(B.new_mode_fire_rate_entry.get());C=B.new_mode_hotkey_entry.get();D=B.new_mode_name_entry.get()
                try:
                        if keyboard.is_pressed(C):0
                except:C=_H;print('INVALID HOTKEY FOR THE NEW MODE')
                if A<80:A=80
                elif A>1000:A=1000
                E={_L:D,_F:A,_G:C};B.config_class.edit_config(f"[modes][{D}]",E,action=_j)
        def save_preferences(A):
                try:A.config_class.edit_config(f"[preferences][hold_key]",A.hold_key_entry.get(),action=_N);A.config_class.edit_config(f"[preferences][menu_key]",A.menu_key_entry.get(),action=_N);A.config_class.edit_config(f"[preferences][hold_to_toggle]",A.hold_to_toggle_checkbox.get(),action=_N);A.config_class.edit_config(f"[preferences][mute]",A.mute_checkbox.get(),action=_N);A.config_class.edit_config(f"[preferences][shoot_when_moving_hotkey]",A.shoot_when_moving_hotkey_entry.get(),action=_N);A.config_class.edit_config(f"[preferences][on_off_hotkey]",A.on_off_hotkey_entry.get(),action=_N)
                except Exception as B:print(B)
        def refresh_config_gui_from_config_file(A):
                A.config_class.load_config();A.config=A.config_class.config;gui.update_modes_dropdown()
                for B in A.mode_editor_tab.winfo_children():B.destroy()
                for B in A.mode_creator_tab.winfo_children():B.destroy()
                for B in A.preferences_tab.winfo_children():B.destroy()
                A.setup_preferences_tab();A.setup_mode_editor_tab();A.setup_mode_creator_tab()
class GUI:
        def __init__(A,root):A.root=root;A.root.title('v4.1_.mp4 - VLC media player');A.root.attributes(_n,_C);A.root.option_add('*Font',('Nunito',14,_B));A.root.geometry('381x281');A.active_values=active_values;A.auth=auth;A.log=log;A.config_gui=config_gui;A.config=config;A.create_widgets();A.camera=camera
        def create_widgets(A):
                F='yellow';E='#00FF00';D='ON/OFF';C='on';B='consola';A.toggle_text=customtkinter.CTkLabel(root,text='Toggle',font=(B,14,_B));A.toggle_text.grid(row=0,column=0,padx=10,pady=20,sticky=_A);A.switch_var=customtkinter.StringVar(value=C);A.switch=customtkinter.CTkSwitch(A.root,text=D,command=A.switch_event,variable=A.switch_var,onvalue=C,offvalue=_g,progress_color=E);A.switch.grid(row=0,column=1,padx=10,pady=20,sticky=_A);A.wpn_text=customtkinter.CTkLabel(root,text='mode',font=(B,14,_B));A.wpn_text.grid(row=0,column=2,padx=10,pady=20,sticky=_A);A.optionmenu=customtkinter.CTkOptionMenu(A.root,width=100,values=active_values.modes,command=A.optionmenu_callback);A.optionmenu.set(A.optionmenu._values[0]if A.optionmenu._values else _T);active_values.latency=int(A.config.config[_J][A.optionmenu.get()][_F]);A.optionmenu.grid(row=1,column=2,padx=(10,0),pady=(0,20),sticky=_A);A.slidertext=customtkinter.CTkLabel(root,text='detection area ',font=(B,14,_B));A.slidertext.grid(row=6,column=0,padx=10,pady=(0,20),sticky=_A);A.slider_value=customtkinter.CTkLabel(root,text='8',font=(B,14,_B));A.slider_value.grid(row=6,column=1,padx=(80,0),pady=(0,20),sticky=_A);A.slider=customtkinter.CTkSlider(A.root,number_of_steps=3,from_=1,to=4,width=60,command=A.slider_event);A.slider.set(active_values.grabzone);A.slider_event(active_values.grabzone);A.slider.grid(row=6,column=1,padx=10,pady=(0,20),sticky=_A);A.color_text=customtkinter.CTkLabel(root,text='color',font=(B,14,_B));A.color_text.grid(row=2,column=0,padx=10,pady=5,sticky=_A);A.radio_var=tkinter.IntVar(value=1);A.radiobutton_1=customtkinter.CTkRadioButton(A.root,text=F,command=A.radiobutton_event,fg_color=F,variable=A.radio_var,value=0);A.radiobutton_2=customtkinter.CTkRadioButton(A.root,text='purple',command=A.radiobutton_event,fg_color='#7b00ff',variable=A.radio_var,value=1);A.radiobutton_1.grid(row=2,column=1,padx=10,pady=(20,0),sticky=_A);A.radiobutton_2.grid(row=3,column=1,padx=10,pady=0,sticky=_A);A.monitor_text=customtkinter.CTkLabel(root,text='monitor',font=(B,14,_B));A.monitor_text.grid(row=2,column=2,padx=10,pady=(0,20),sticky=_A);A.monitor_optionmenu=customtkinter.CTkSegmentedButton(A.root,values=active_values.formatted,command=A.monitor_optionmenu_callback);A.monitor_optionmenu.set(active_values.formatted[0]);A.monitor_optionmenu.grid(row=3,column=2,padx=10,pady=0,sticky=_A);A.moving_text=customtkinter.CTkLabel(root,text='shoot when moving',wraplength=100,font=(B,14,_B));A.moving_text.grid(row=1,column=0,padx=10,pady=0,sticky=_A);A.moving_var=customtkinter.StringVar(value=_g);A.moving=customtkinter.CTkSwitch(A.root,text=D,command=A.moving_event,variable=A.moving_var,onvalue=C,offvalue=_g,progress_color=E);A.moving.grid(row=1,column=1,padx=10,pady=10,sticky=_A)
                if A.active_values.user_type==_k:A.reload_config_text=customtkinter.CTkLabel(A.root,text='config',font=(B,14,_B));A.reload_config_text.grid(row=6,column=2,padx=10,pady=10,sticky=_A);A.reload_config_button=customtkinter.CTkButton(A.root,text='open',width=20,font=(B,13,_B),command=show_config_gui);A.reload_config_button.grid(row=6,column=2,padx=60,pady=10,sticky=_A)
        def update_modes_dropdown(A):A.optionmenu.set('');A.optionmenu.configure(values=A.active_values.modes);A.optionmenu.set(A.optionmenu._values[0]if A.optionmenu._values else _T);active_values.latency=int(A.config.config[_J][A.optionmenu.get()][_F])
        def moving_event_keyboard(A):A.moving.toggle()
        def moving_event(A):
                print('moving toggled,  value:',A.moving_var.get());log.write_to_log(f"moving toggled,  value: {A.moving_var.get()}")
                if A.moving_var.get()==_g:active_values.shoot_when_moving=_E
                else:active_values.shoot_when_moving=_C
        def switch_event_keyboard(A):A.log.write_to_log(f"switch toggled, current value: {A.switch_var.get()}");A.switch.toggle()
        def switch_event(A):print(active_values.toggle);print(not active_values.toggle);active_values.toggle=not active_values.toggle;print('switch toggled, current value:',A.switch_var.get());log.write_to_log(f"switch toggled, current value: {A.switch_var.get()}")
        def optionmenu_callback(B,choice):
                A=choice;B.optionmenu.set(A)
                if A==_l:print('sniper mode - only shooting if scoped');active_values.sniper_mode=_C;active_values.burst_mode=_E
                elif A==_m:active_values.sniper_mode=_E;active_values.burst_mode=_C
                else:active_values.sniper_mode=_E;active_values.burst_mode=_E
                print('optionmenu dropdown clicked:',A);log.write_to_log(f"optionmenu dropdown clicked: {A} ");active_values.latency=int(B.config.config[_J][A][_F]);print(active_values.latency)
        def slider_event(B,value):A=value;active_values.grabzone=int(A);B.slider_value.configure(text=int(A))
        def radiobutton_event(A):active_values.colorSelected=A.radio_var.get();print('radiobutton toggled, value:',A.radio_var.get());print('selected color:',active_values.colorSelected);log.write_to_log(f"selected color: {active_values.colorSelected} ")
        def monitor_optionmenu_callback(A,choice):A.monitor_optionmenu.set(choice);import re;B=int(re.search('\\d+',A.monitor_optionmenu.get()).group());active_values.selectedMonitorIndex=B*-1;print('monitor index selected:',active_values.selectedMonitorIndex);log.write_to_log(f"monitor index selected: {active_values.selectedMonitorIndex}");A.camera.set_center_from_selected_monitor()
        def monitor_optionmenu_callback_default(A):A.monitor_optionmenu_callback(active_values.formatted[0])
def show_config_gui():A=customtkinter.CTk();B=CONFIG_GUI(A,config);A.mainloop()
class LOG:
        def __init__(A):A.active_values=active_values
        import os;script_dir=os.path.dirname(os.path.abspath(__file__));log_file_path=os.path.join(script_dir,'turbo_log.txt');import datetime;current_utc_datetime=datetime.datetime.now(datetime.timezone.utc)
        with open(log_file_path,'a')as log_file:log_file.write('STARTING NEW SESSTION ['+str(current_utc_datetime)+']'+'\n')
        def write_to_log(A,message):
                with open(A.log_file_path,'a')as B:B.write(message+'\n')
active_values=ActiveValues()
log=LOG()
camera=Camera()
auth=Auth()
config=Config(active_values)
root=customtkinter.CTk()
config_root=customtkinter.CTk()
config_gui=CONFIG_GUI(config_root,config)
gui=GUI(root)
gui.monitor_optionmenu_callback_default()
def is_moving():
        A='d';B={_A:(0,-1),'s':(0,1),'a':(-1,0),A:(1,0),'z':(0,-1),'q':(-1,0)};C=[(A,'a'),(A,'q')]
        for(D,E)in C:
                if keyboard.is_pressed(D)and keyboard.is_pressed(E):return _E
        for F in B.keys():
                if keyboard.is_pressed(F):return _C
        return _E
class HOTKEYS:
        def __init__(A):A.config=config;A.mode_hotkeys_thread=threading.Thread(target=A.listen_to_mode_hotkeys,daemon=_C);A.mode_hotkeys_thread.start();A.gui=gui;A.active_values=active_values
        def beep(A,freq,duration):
                if config.config[_D][_a]==_C:return
                winsound.Beep(freq,duration)
        def listen_to_mode_hotkeys(A):
                C='pressed --> '
                while _C:
                        time.sleep(.05)
                        for D in config.config[_J]:
                                B=config.config[_J][D][_G];E=config.config[_J][D][_L]
                                if B!=_H and B!='Null'and B!='':
                                        if keyboard.is_pressed(B):A.beep(200,150);gui.optionmenu_callback(E);print(C,B)
                        if keyboard.is_pressed(config.config[_D][_R]):
                                if active_values.toggle:A.beep(200,150)
                                else:A.beep(600,75)
                                gui.switch_event_keyboard();print(C,config.config[_D][_R])
                                while keyboard.is_pressed(config.config[_D][_R]):continue
                        if keyboard.is_pressed(config.config[_D][_Q]):
                                if active_values.shoot_when_moving:A.beep(200,150)
                                else:A.beep(600,75)
                                gui.moving_event_keyboard();print(C,config.config[_D][_Q])
                                while keyboard.is_pressed(config.config[_D][_Q]):continue
import threading,queue,time,random,ctypes
INPUT_MOUSE=0
MOUSEEVENTF_LEFTDOWN=2
MOUSEEVENTF_LEFTUP=4
class MOUSEINPUT(ctypes.Structure):_fields_=[('dx',ctypes.c_long),('dy',ctypes.c_long),('mouseData',ctypes.c_ulong),('dwFlags',ctypes.c_ulong),('time',ctypes.c_ulong),('dwExtraInfo',ctypes.POINTER(ctypes.c_ulong))]
class INPUT(ctypes.Structure):_fields_=[('type',ctypes.c_ulong),('mi',MOUSEINPUT)]
def send_mouse_input(flags):B=ctypes.c_ulong(0);C=MOUSEINPUT(0,0,0,flags,0,ctypes.pointer(B));A=INPUT(INPUT_MOUSE,C);ctypes.windll.user32.SendInput(1,ctypes.pointer(A),ctypes.sizeof(A))
class ClickHandler:
        def __init__(A):A.active_values=active_values
        def generate_random_number(A,n):return random.randint(n-20,n+20)
        def request_click(A):import pyautogui as B;C=random.uniform(.05,.15);B.click(button=_P);time.sleep(A.generate_random_number(A.active_values.latency)/1000)
clicker=ClickHandler()
class BOT:
        def __init__(A):A.active_values=active_values;A.camera=camera;A.config=config;A.log=log;A.clicker=clicker;A.MOUSE_BUTTON_4=1;A.MOUSE_BUTTON_5=2;A.MOUSE_BUTTON_3=8;A.game=win32gui.FindWindow(_O,_r)
        def get_mouse_button_state(B):
                A=win32api.GetKeyState(win32con.VK_XBUTTON1)
                if A<0:return B.MOUSE_BUTTON_4
                A=win32api.GetKeyState(win32con.VK_XBUTTON2)
                if A<0:return B.MOUSE_BUTTON_5
                A=win32api.GetKeyState(win32con.VK_RBUTTON)
                if A<0:return B.MOUSE_BUTTON_3
        def add_to_banner(D,message):
                C=' ';B=message;A='┃ ';A+=int(14-len(B)/2)*C;A+=B;A+=int(14-len(B)/2)*C
                while len(A)<30:A+=C
                A+='┃\n';A+='╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋';print(A)
        def print_banner(A):print('\n\n              \n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n┃        ┓        •           ┃\n┃   ╋┓┏┏┓┣┓┏┓  ╋┏┓┓┏┓┏┓┏┓┏┓   ┃ \n┃   ┗┗┻┛ ┗┛┗┛  ┗┛ ┗┗┫┗┫┗ ┛    ┃\n┃                   ┛ ┛       ┃\n╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋');A.add_to_banner('running in '+active_values.user_type)
        def click(A):
                try:
                        if A.game==0 or A.game==_O:A.game=win32gui.FindWindow(_O,_r)
                        print(A.game);B=random.uniform(.05,.15);win32gui.PostMessage(A.game,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,0);time.sleep(B);win32gui.PostMessage(A.game,win32con.WM_LBUTTONUP,0,0);log.write_to_log('calling send_data_to_client the signal')
                except Exception as C:print(f"An error occurred: {C}");A.game=win32gui.FindWindow(_O,_r)
        def main(A):
                G='clicked';F='normal';E='withdrawn';D='HOLD key is : ';A.print_banner();A.add_to_banner('HOLD <'+config.config[_D][_S]+'> to show menu')
                if config.config[_D][_W]==_C:A.add_to_banner(D+config.config[_D][_K]);log.write_to_log('HOLD to toggle is on');log.write_to_log(D+config.config[_D][_K])
                log.write_to_log(str(active_values.formatted))
                if active_values.connected:A.add_to_banner('connected')
                while _C:
                        if keyboard.is_pressed(config.config[_D][_S]):
                                if root.state()==E:root.state(F)
                                else:time.sleep(1)
                        elif root.state()==F:root.state(E)
                        if not active_values.toggle:log.write_to_log('Toggled OFF');time.sleep(.01);continue
                        if config.config[_D][_W]==_C:
                                try:
                                        if config.config[_D][_K]==_e:
                                                if not A.get_mouse_button_state()==A.MOUSE_BUTTON_4:time.sleep(.01);continue
                                        elif config.config[_D][_K]==_h:
                                                if not A.get_mouse_button_state()==A.MOUSE_BUTTON_5:time.sleep(.01);continue
                                        elif config.config[_D][_K]==_i:
                                                if not A.get_mouse_button_state()==A.MOUSE_BUTTON_3:time.sleep(.01);continue
                                        elif config.config[_D][_K]==_H:print('error : HOLD MODE IS ON BUT YOU DONT HAVE A HOLD KEY REGISTERED , ADD A HOLD KEY OR CONTACT SUPPORT');time.sleep(.01);continue
                                        elif not keyboard.is_pressed(config.config[_D][_K]):time.sleep(.01);continue
                                except Exception as B:print(B);log.write_to_log(str(B))
                        active_values.last_frame_moving=active_values.moving
                        if is_moving():active_values.moving=_C
                        else:active_values.moving=_E
                        if active_values.last_frame_moving and not active_values.moving and not active_values.shoot_when_moving:time.sleep(.1)
                        if not active_values.shoot_when_moving and active_values.moving:continue
                        H=1;I=win32api.GetKeyState(H)
                        if I<0:log.write_to_log('left mouse button clicked');time.sleep(.3);continue
                        M=_E;C=camera.grab_method2()
                        if C:
                                N,O,J,K,L=C
                                if not active_values.sniper_mode or camera.check_for_white(J,K,L):
                                        if active_values.burst_mode:A.click();time.sleep(A.generate_random_number(75)/1000*2);A.click();time.sleep(A.generate_random_number(75)/1000*2);A.click();log.write_to_log('found a matching pixel (burst)');print(G)
                                        else:A.click();log.write_to_log('found a matching pixel');print(G)
                                        P=_C
        def generate_random_number(B,n):A=random.randint(n-20,n+20);return A
bot=BOT()
hotkeys=HOTKEYS()
main_thread=threading.Thread(target=bot.main,daemon=_C)
main_thread.start()
root.mainloop()

import json
import os

CONFIG_FILE = "config.json"

# デフォルト設定
default_config = {
    "fire_rate": 100,          # 連射速度(ms)
    "hotkey": "ctrl+shift",    # 発射トリガーのホットキー
    "mode": "burst",           # モード (burst, sniper, custom)
    "sound_enabled": True      # 効果音 ON/OFF
}

# 設定を読み込み
def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Config Error] 読み込みに失敗しました: {e}")
            return default_config.copy()
    else:
        return default_config.copy()

# 設定を保存
def save_config(config):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        print("[Config] 設定を保存しました。")
    except Exception as e:
        print(f"[Config Error] 保存に失敗しました: {e}")
def on_save_button_click():
            config["fire_rate"] = fire_rate_slider.get()
            config["hotkey"] = hotkey_entry.get()
            config["mode"] = mode_var.get()
            config["sound_enabled"] = sound_check_var.get()
            save_config(config)
            
config = load_config()

import os
import sys
import json
import time
import random
import logging
import threading
import subprocess
import tkinter as tk
import tkinter.messagebox as messagebox

# 必須ライブラリ
required_packages = [
    "mss", "Pillow", "colorsys", "tkinter",
    "winsound", "requests", "threading", "customtkinter",
    "keyboard", "pywin32"
]

# ========== ライブラリ管理 ==========
def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        log_info(f"[Install] {package} をインストールしました。")
    except Exception as e:
        log_error(f"[Install Error] {package} のインストールに失敗: {e}")

def check_and_install_packages(packages):
    for pkg in packages:
        try:
            __import__(pkg)
        except ImportError:
            if pkg == "Pillow":
                pkg = "Pillow"
            if pkg == "pywin32":
                pkg = "pypiwin32"
            install(pkg)

# ========== ログ管理 ==========
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    encoding="utf-8"
)

def log_info(msg):
    print(msg)
    logging.info(msg)

def log_error(msg):
    print(f"[ERROR] {msg}")
    logging.error(msg)

# ========== 設定管理 ==========
CONFIG_FILE = "config.json"

default_config = {
    "fire_rate": 100,          # 連射速度(ms)
    "hotkey": "ctrl+shift",    # 発射トリガーのホットキー
    "mode": "burst",           # モード (burst, sniper, custom)
    "sound_enabled": True      # 効果音 ON/OFF
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                config = json.load(f)
            log_info("[Config] 設定を読み込みました。")
            return config
        except Exception as e:
            log_error(f"[Config Error] 読み込み失敗: {e}")
            return default_config.copy()
    else:
        log_info("[Config] 新しい設定ファイルを作成します。")
        return default_config.copy()

def save_config(config):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        log_info("[Config] 設定を保存しました。")
    except Exception as e:
        log_error(f"[Config Error] 保存失敗: {e}")

# ========== GUI構築 ==========
class TurboTriggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TurboTrigger Revamped")
        self.root.geometry("400x300")

        self.config = load_config()

        # fire_rate
        tk.Label(root, text="連射速度 (ms)").pack()
        self.fire_rate_slider = tk.Scale(root, from_=50, to=1000, orient="horizontal")
        self.fire_rate_slider.set(self.config["fire_rate"])
        self.fire_rate_slider.pack()

        # hotkey
        tk.Label(root, text="ホットキー").pack()
        self.hotkey_entry = tk.Entry(root)
        self.hotkey_entry.insert(0, self.config["hotkey"])
        self.hotkey_entry.pack()

        # mode
        tk.Label(root, text="モード").pack()
        self.mode_var = tk.StringVar(value=self.config["mode"])
        tk.OptionMenu(root, self.mode_var, "burst", "sniper", "custom").pack()

        # sound
        self.sound_check_var = tk.BooleanVar(value=self.config["sound_enabled"])
        tk.Checkbutton(root, text="効果音 ON", variable=self.sound_check_var).pack()

        # 保存ボタン
        tk.Button(root, text="設定を保存", command=self.on_save_button_click).pack(pady=10)

    def on_save_button_click(self):
        self.config["fire_rate"] = self.fire_rate_slider.get()
        self.config["hotkey"] = self.hotkey_entry.get()
        self.config["mode"] = self.mode_var.get()
        self.config["sound_enabled"] = self.sound_check_var.get()
        save_config(self.config)
        messagebox.showinfo("保存完了", "設定を保存しました。")

# ========== 実行 ==========
if __name__ == "__main__":
    check_and_install_packages(required_packages)
    log_info("TurboTrigger Revamped を起動しました。")

    root = tk.Tk()
    app = TurboTriggerApp(root)
    root.mainloop()
import os
        import sys
        import json
        import time
        import logging
        import threading
        import subprocess
        import tkinter as tk
        import tkinter.messagebox as messagebox
        import requests  # アップデートチェック用
        
        # ====== バージョン ======
        CURRENT_VERSION = "1.0.0"
        UPDATE_URL = "https://raw.githubusercontent.com/yourname/yourrepo/main/version.json"
        # ↑ GitHub等に { "latest": "1.0.1", "changelog": "修正内容..." } を置く
        
        # ====== 必須ライブラリ ======
        required_packages = [
            "mss", "Pillow", "colorsys", "tkinter",
            "winsound", "requests", "threading", "customtkinter",
            "keyboard", "pywin32"
        ]
        
        # ====== ライブラリ管理 ======
        def install(package):
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                log_info(f"[Install] {package} をインストールしました。")
            except Exception as e:
                log_error(f"[Install Error] {package} のインストールに失敗: {e}")
        
        def check_and_install_packages(packages):
            for pkg in packages:
                try:
                    __import__(pkg)
                except ImportError:
                    if pkg == "Pillow":
                        pkg = "Pillow"
                    if pkg == "pywin32":
                        pkg = "pypiwin32"
                    install(pkg)
        
        # ====== ログ管理 ======
        LOG_DIR = "logs"
        LOG_FILE = os.path.join(LOG_DIR, "app.log")
        os.makedirs(LOG_DIR, exist_ok=True)
        
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            encoding="utf-8"
        )
        
        def log_info(msg):
            print(msg)
            logging.info(msg)
        
        def log_error(msg):
            print(f"[ERROR] {msg}")
            logging.error(msg)
        
        # ====== 設定管理 ======
        CONFIG_FILE = "config.json"
        
        default_config = {
            "fire_rate": 100,
            "hotkey": "ctrl+shift",
            "mode": "burst",
            "sound_enabled": True
        }
        
        def load_config():
            if os.path.exists(CONFIG_FILE):
                try:
                    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                        config = json.load(f)
                    log_info("[Config] 設定を読み込みました。")
                    return config
                except Exception as e:
                    log_error(f"[Config Error] 読み込み失敗: {e}")
                    return default_config.copy()
            else:
                log_info("[Config] 新しい設定ファイルを作成します。")
                return default_config.copy()
        
        def save_config(config):
            try:
                with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                    json.dump(config, f, indent=4, ensure_ascii=False)
                log_info("[Config] 設定を保存しました。")
            except Exception as e:
                log_error(f"[Config Error] 保存失敗: {e}")
        
        # ====== アップデートチェック ======
        def check_update():
            try:
                log_info("[Update] アップデートを確認中...")
                res = requests.get(UPDATE_URL, timeout=5)
                if res.status_code == 200:
                    data = res.json()
                    latest = data.get("latest")
                    changelog = data.get("changelog", "")
                    if latest and latest != CURRENT_VERSION:
                        msg = f"新しいバージョン {latest} が利用可能です！\n\n変更内容:\n{changelog}"
                        log_info(f"[Update] {msg}")
                        messagebox.showinfo("アップデート通知", msg)
                    else:
                        log_info("[Update] 最新バージョンを利用中です。")
                else:
                    log_error(f"[Update Error] ステータスコード {res.status_code}")
            except Exception as e:
                log_error(f"[Update Error] {e}")
        
        # ====== GUI構築 ======
        class TurboTriggerApp:
            def __init__(self, root):
                self.root = root
                self.root.title(f"TurboTrigger Revamped v{CURRENT_VERSION}")
                self.root.geometry("400x300")
        
                self.config = load_config()
        
                # fire_rate
                tk.Label(root, text="連射速度 (ms)").pack()
                self.fire_rate_slider = tk.Scale(root, from_=50, to=1000, orient="horizontal")
                self.fire_rate_slider.set(self.config["fire_rate"])
                self.fire_rate_slider.pack()
        
                # hotkey
                tk.Label(root, text="ホットキー").pack()
                self.hotkey_entry = tk.Entry(root)
                self.hotkey_entry.insert(0, self.config["hotkey"])
                self.hotkey_entry.pack()
        
                # mode
                tk.Label(root, text="モード").pack()
                self.mode_var = tk.StringVar(value=self.config["mode"])
                tk.OptionMenu(root, self.mode_var, "burst", "sniper", "custom").pack()
        
                # sound
                self.sound_check_var = tk.BooleanVar(value=self.config["sound_enabled"])
                tk.Checkbutton(root, text="効果音 ON", variable=self.sound_check_var).pack()
        
                # 保存ボタン
                tk.Button(root, text="設定を保存", command=self.on_save_button_click).pack(pady=10)
        
                # アップデート確認ボタン
                tk.Button(root, text="アップデート確認", command=check_update).pack(pady=5)
        
            def on_save_button_click(self):
                self.config["fire_rate"] = self.fire_rate_slider.get()
                self.config["hotkey"] = self.hotkey_entry.get()
                self.config["mode"] = self.mode_var.get()
                self.config["sound_enabled"] = self.sound_check_var.get()
                save_config(self.config)
                messagebox.showinfo("保存完了", "設定を保存しました。")
        
        # ====== 実行 ======
        if __name__ == "__main__":
            check_and_install_packages(required_packages)
            log_info("TurboTrigger Revamped を起動しました。")
        
            root = tk.Tk()
            app = TurboTriggerApp(root)
        
            # 起動時に自動アップデートチェック
            threading.Thread(target=check_update, daemon=True).start()
        
            root.mainloop()
CURRENT_VERSION = "1.0.0"
            UPDATE_URL = "https://raw.githubusercontent.com/<ユーザー名>/<リポジトリ名>/main/version.json"
UPDATE_URL = "https://raw.githubusercontent.com/HarukiDev/TurboTriggerRev/main/version.json"





            
        